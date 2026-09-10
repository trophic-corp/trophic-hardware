# ECP-01 Fusion change script for CEA_RACK_INTEGRATED_v2 v8 -> v9.
# Executed in chunks via the Fusion MCP. Each STEP function is idempotent (checks component names first)
# and prints a one-line JSON result. All coordinates mm, converted to cm (Fusion internal).
import adsk.core, adsk.fusion, json, math, traceback
app = adsk.core.Application.get()
des = adsk.fusion.Design.cast(app.activeProduct)
root = des.rootComponent
U = 0.1
GI = 'Steel, Galvanized'
SS = 'Stainless Steel AISI 304'
V = adsk.core.ValueInput.createByReal
P3 = adsk.core.Point3D.create

def mat(name):
    m = des.materials.itemByName(name)
    if m: return m
    for lib in app.materialLibraries:
        try:
            mm = lib.materials.itemByName(name)
            if mm: return mm
        except: pass
    return None

def names():
    return set(o.component.name for o in root.allOccurrences)

def new_comp(name):
    occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    occ.component.name = name
    return occ

def plane_z(comp, z):
    pi = comp.constructionPlanes.createInput()
    pi.setByOffset(root.xYConstructionPlane, V(z*U))
    return comp.constructionPlanes.add(pi)

def box(comp, x0,x1,y0,y1,z0,z1, op='new'):
    """Axis-aligned box: sketch rect on plane at z0, extrude to z1."""
    pl = plane_z(comp, z0)
    sk = comp.sketches.add(pl)
    a = sk.modelToSketchSpace(P3(x0*U,y0*U,z0*U)); b = sk.modelToSketchSpace(P3(x1*U,y1*U,z0*U))
    sk.sketchCurves.sketchLines.addTwoPointRectangle(a, b)
    prof = sk.profiles.item(0)
    opn = {'new':adsk.fusion.FeatureOperations.NewBodyFeatureOperation,'cut':adsk.fusion.FeatureOperations.CutFeatureOperation,'join':adsk.fusion.FeatureOperations.JoinFeatureOperation}[op]
    inp = comp.features.extrudeFeatures.createInput(prof, opn)
    inp.setDistanceExtent(False, V((z1-z0)*U))
    f = comp.features.extrudeFeatures.add(inp)
    # direction check: if extruded the wrong way, flip
    bb = comp.bRepBodies.item(comp.bRepBodies.count-1).boundingBox if op=='new' else None
    if op=='new' and bb and (bb.maxPoint.z*10 < z0+0.5):
        f.deleteMe(); sk.deleteMe()
        sk = comp.sketches.add(pl)
        sk.sketchCurves.sketchLines.addTwoPointRectangle(a, b)
        inp = comp.features.extrudeFeatures.createInput(sk.profiles.item(0), opn)
        inp.setDistanceExtent(False, V(-(z1-z0)*U))
        f = comp.features.extrudeFeatures.add(inp)
    return f

def cyl_cut(comp, cx, cy, z0, z1, dia, axis='z'):
    """Cylindrical cut along Z through z0..z1 at (cx,cy)."""
    pl = plane_z(comp, z0-1)
    sk = comp.sketches.add(pl)
    c = sk.modelToSketchSpace(P3(cx*U,cy*U,(z0-1)*U))
    sk.sketchCurves.sketchCircles.addByCenterRadius(c, dia/2*U)
    inp = comp.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
    inp.setSymmetricExtent(V((z1-z0+2)*U), True)
    inp.setDistanceExtent(False, V((z1-z0+2)*U))
    try:
        return comp.features.extrudeFeatures.add(inp)
    except:
        inp = comp.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
        inp.setDistanceExtent(False, V(-(z1-z0+2)*U))
        return comp.features.extrudeFeatures.add(inp)

def shs(comp, x0,x1,y0,y1,z0,z1, t):
    """Hollow section box (axis along the longest side) built as outer box minus inner box."""
    box(comp, x0,x1,y0,y1,z0,z1,'new')
    dx,dy,dz = x1-x0, y1-y0, z1-z0
    if dz >= dx and dz >= dy:      # vertical
        box(comp, x0+t,x1-t,y0+t,y1-t,z0-1,z1+1,'cut')
    elif dx >= dy:                 # along X
        box(comp, x0-1,x1+1,y0+t,y1-t,z0+t,z1-t,'cut')
    else:                          # along Y
        box(comp, x0+t,x1-t,y0-1,y1+1,z0+t,z1-t,'cut')

def set_mat(comp, name):
    m = mat(name)
    if m:
        for b in comp.bRepBodies: b.material = m

def delete_named(name):
    n=0
    for o in list(root.allOccurrences):
        if o.component.name == name:
            o.deleteMe(); n+=1
    return n

def bar(comp, p1, p2, width, y0, y1, holes, dia):
    """Flat bar in the XZ plane between centreline points p1,p2 (x,z), thickness y0..y1, with holes at 'holes' [(x,z)]."""
    (x1,z1),(x2,z2) = p1,p2
    L = math.hypot(x2-x1, z2-z1); ux,uz = (x2-x1)/L, (z2-z1)/L
    nx,nz = -uz, ux
    w = width/2
    pts = [(x1+nx*w, z1+nz*w),(x2+nx*w, z2+nz*w),(x2-nx*w, z2-nz*w),(x1-nx*w, z1-nz*w)]
    pi = comp.constructionPlanes.createInput(); pi.setByOffset(root.xZConstructionPlane, V(y0*U))
    pl = comp.constructionPlanes.add(pi)
    sk = comp.sketches.add(pl)
    sp = [sk.modelToSketchSpace(P3(x*U, y0*U, z*U)) for (x,z) in pts]
    lines = sk.sketchCurves.sketchLines
    for i in range(4): lines.addByTwoPoints(sp[i], sp[(i+1)%4])
    for (hx,hz) in holes:
        sk.sketchCurves.sketchCircles.addByCenterRadius(sk.modelToSketchSpace(P3(hx*U,y0*U,hz*U)), dia/2*U)
    # profile with holes = the one with largest area
    prof = max([sk.profiles.item(i) for i in range(sk.profiles.count)], key=lambda p: p.areaProperties().area)
    inp = comp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    inp.setDistanceExtent(False, V((y1-y0)*U))
    f = comp.features.extrudeFeatures.add(inp)
    bb = comp.bRepBodies.item(0).boundingBox
    if abs(bb.minPoint.y*10 - y0) > 0.5:   # extruded the wrong way -> redo negative
        f.deleteMe()
        inp = comp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        inp.setDistanceExtent(False, V(-(y1-y0)*U))
        f = comp.features.extrudeFeatures.add(inp)
    return f

def bbox_of(name):
    for o in root.allOccurrences:
        if o.component.name == name:
            bb=o.boundingBox; return [round(bb.minPoint.x*10,1),round(bb.maxPoint.x*10,1),round(bb.minPoint.y*10,1),round(bb.maxPoint.y*10,1),round(bb.minPoint.z*10,1),round(bb.maxPoint.z*10,1)]


def place(comp_name, dx, dy, dz):
    """Add another occurrence of an existing component translated by (dx,dy,dz) mm from where it was built."""
    comp=None
    for o in root.allOccurrences:
        if o.component.name==comp_name: comp=o.component; break
    m=adsk.core.Matrix3D.create(); m.translation=adsk.core.Vector3D.create(dx*U,dy*U,dz*U)
    return root.occurrences.addExistingComponent(comp, m)

def build_series(name, build_fn, positions):
    """build_fn(comp) builds the part at positions[0] (absolute); further positions are placed by translation."""
    if name in names(): return 0
    occ=new_comp(name); build_fn(occ.component)
    x0,y0,z0=positions[0]
    for (x,y,z) in positions[1:]:
        place(name, x-x0, y-y0, z-z0)
    return len(positions)

# ---------------------------------------------------------------- STEPS
def step_C1_cross_beams():
    pos=[(x,40,z) for z in (243.4,643.4,1043.4,1443.4) for x in (0,1226)]
    def b(c): shs(c,0,30,40,520,243.4,273.4,1.5); set_mat(c,GI)
    return build_series('03_BEAM_SHORT_TIER', b, pos)

def plate_yz(comp, x0,x1, y0,y1, z0,z1, holes, dia=9):
    """Flat plate in a YZ plane (thickness x0..x1) with holes [(y,z)]."""
    pi=comp.constructionPlanes.createInput(); pi.setByOffset(root.yZConstructionPlane, V(x0*U)); pl=comp.constructionPlanes.add(pi)
    sk=comp.sketches.add(pl)
    a=sk.modelToSketchSpace(P3(x0*U,y0*U,z0*U)); b=sk.modelToSketchSpace(P3(x0*U,y1*U,z1*U))
    sk.sketchCurves.sketchLines.addTwoPointRectangle(a,b)
    for (hy,hz) in holes: sk.sketchCurves.sketchCircles.addByCenterRadius(sk.modelToSketchSpace(P3(x0*U,hy*U,hz*U)), dia/2*U)
    prof=max([sk.profiles.item(i) for i in range(sk.profiles.count)], key=lambda p:p.areaProperties().area)
    inp=comp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation); inp.setDistanceExtent(False, V((x1-x0)*U))
    f=comp.features.extrudeFeatures.add(inp); bb=comp.bRepBodies.item(0).boundingBox
    if abs(bb.minPoint.x*10-x0)>0.5:
        f.deleteMe(); inp=comp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation); inp.setDistanceExtent(False, V(-(x1-x0)*U)); f=comp.features.extrudeFeatures.add(inp)
    return f

def plate_xz(comp, x0,x1, y0,y1, z0,z1, holes, dia=9):
    zc=(z0+z1)/2
    return bar(comp,(x0,zc),(x1,zc),z1-z0,y0,y1,holes,dia)

def step_C2_C3_C4_brackets():
    """RK-A-107B flat gusset plates (3 mm GI) at every beam end: 2 x M8 into rivet nuts on the post face + 2 x M8 through the beam
    end holes (25/75 from the end) with crush tubes. Long beams: plates on the front (Y -3..0) and rear (Y 560..563) faces.
    Cross beams: plates on the outer X faces (X -3..0 and 1256..1259)."""
    made={}
    tiers=[243.4,643.4,1043.4,1443.4]
    # ---- long beam plates, tiers: rows zb+6.6 and zb-43.4 on the post (X 20 / 1236); beam holes at X 65,115 / 1141,1191, Z zb+15
    def lbL(c): plate_xz(c,0,140,-3,0,243.4-58,243.4+30,[(20,250),(20,200),(65,258.4),(115,258.4)]); set_mat(c,GI)
    def lbR(c): plate_xz(c,1116,1256,-3,0,243.4-58,243.4+30,[(1236,250),(1236,200),(1191,258.4),(1141,258.4)]); set_mat(c,GI)
    posL=[(0,y,z) for z in tiers for y in (-3,560)]
    made['PL_107B_LB_L']=build_series('03_PL107B_LB_L', lbL, posL)
    made['PL_107B_LB_R']=build_series('03_PL107B_LB_R', lbR, [(1116,y,z) for z in tiers for y in (-3,560)])
    # base long beams (Z 150-180): rows 150 & 200 on the post; beam holes at Z 165
    def lbLb(c): plate_xz(c,0,140,-3,0,135,215,[(20,150),(20,200),(65,165),(115,165)]); set_mat(c,GI)
    def lbRb(c): plate_xz(c,1116,1256,-3,0,135,215,[(1236,150),(1236,200),(1191,165),(1141,165)]); set_mat(c,GI)
    made['PL_107B_LB_L_BASE']=build_series('03_PL107B_LB_L_BASE', lbLb, [(0,-3,135),(0,560,135)])
    made['PL_107B_LB_R_BASE']=build_series('03_PL107B_LB_R_BASE', lbRb, [(1116,-3,135),(1116,560,135)])
    # ---- cross beam plates on the outer X faces. Front end: post Y 0-40 (rows Z zb+6.6 / zb-43.4 at Y 20), beam holes at Y 65,115
    def cbF(c): plate_yz(c,-3,0,0,140,243.4-58,243.4+30,[(20,250),(20,200),(65,258.4),(115,258.4)]); set_mat(c,GI)
    def cbB(c): plate_yz(c,-3,0,420,560,243.4-58,243.4+30,[(540,250),(540,200),(495,258.4),(445,258.4)]); set_mat(c,GI)
    made['PL_107B_CB_F']=build_series('03_PL107B_CB_F', cbF, [(x,0,z) for z in tiers for x in (-3,1256)])
    made['PL_107B_CB_B']=build_series('03_PL107B_CB_B', cbB, [(x,420,z) for z in tiers for x in (-3,1256)])
    def cbFb(c): plate_yz(c,-3,0,0,140,135,215,[(20,150),(20,200),(65,165),(115,165)]); set_mat(c,GI)
    def cbBb(c): plate_yz(c,-3,0,420,560,135,215,[(540,150),(540,200),(495,165),(445,165)]); set_mat(c,GI)
    made['PL_107B_CB_F_BASE']=build_series('03_PL107B_CB_F_BASE', cbFb, [(-3,0,135),(1256,0,135)])
    made['PL_107B_CB_B_BASE']=build_series('03_PL107B_CB_B_BASE', cbBb, [(-3,420,135),(1256,420,135)])
    # ---- crush tubes: Y-direction in long beams (27 long, Y 1.5..28.5), X-direction in cross beams
    def ctY(c): box(c,60,70,1.5,28.5,253.4,263.4,'new'); set_mat(c,SS)
    posY=[(x,y,zb+10) for zb in tiers+[150] for y in (1.5,531.5) for x in (60,110,1136,1186)]
    made['CRUSH_Y']=build_series('15_CRUSH_TUBE_Y', ctY, [(60,1.5,253.4)]+[p for p in posY if p!=(60,1.5,253.4)])
    def ctX(c): box(c,1.5,28.5,60,70,253.4,263.4,'new'); set_mat(c,SS)
    posX=[(x,y,zb+10) for zb in tiers+[150] for x in (1.5,1227.5) for y in (60,110,440,490)]
    made['CRUSH_X']=build_series('15_CRUSH_TUBE_X', ctX, [(1.5,60,253.4)]+[p for p in posX if p!=(1.5,60,253.4)])
    # ---- rivet nuts (M8, body D11 x 12 in the near wall) on post faces: Y-faces for long-beam plates, X-faces for cross-beam plates
    def rnY(c): box(c,14.5,25.5,0,12,244.5,255.5,'new'); set_mat(c,SS)
    rows=[z for zb in tiers for z in (zb+6.6, zb-43.4)] + [150,200]
    posRN=[(x,y,z) for z in rows for x in (14.5,1230.5) for y in (0,548)]
    made['RN_Y']=build_series('15_RIVET_NUT_Y', rnY, [(14.5,0,244.5)]+[(x,y,z-5.5) for (x,y,z) in posRN if (x,y,z)!=(14.5,0,250)])
    def rnX(c): box(c,0,12,14.5,25.5,244.5,255.5,'new'); set_mat(c,SS)
    posRNX=[(x,y,z) for z in rows for y in (14.5,534.5) for x in (0,1244)]
    made['RN_X']=build_series('15_RIVET_NUT_X', rnX, [(0,14.5,244.5)]+[(x,y,z-5.5) for (x,y,z) in posRNX if (x,y,z)!=(0,14.5,250)])
    return made

def step_C5_C6_brace():
    made=[]
    if '05_REAR_BRACE_A' not in names():
        delete_named('05_REAR_BRACE')
        occ=new_comp('05_REAR_BRACE_A'); c=occ.component
        # centreline from hole (20,150) to (1236,1450) extended 15 mm beyond each hole
        ang=math.atan2(1300,1216); ex,ez=15*math.cos(ang),15*math.sin(ang)
        bar(c,(20-ex,150-ez),(1236+ex,1450+ez),25,563,566,[(20,150),(1236,1450)],9); set_mat(c,GI); made.append('A')
        occ=new_comp('05_REAR_BRACE_B'); c=occ.component
        bar(c,(1236+ex,150-ez),(20-ex,1450+ez),25,566,569,[(1236,150),(20,1450)],9); set_mat(c,GI); made.append('B')
        for (hx,hz,y0,y1) in ((20,150,560,563),(1236,1450,560,563),(1236,150,560,566),(20,1450,560,566)):
            occ=new_comp('05_BRACE_PACKER'); c=occ.component
            box(c, hx-20,hx+20, y0,y1, hz-12.5,hz+12.5,'new'); set_mat(c,GI); made.append('P')
    # rear panels 563-565 -> 566-568
    if bbox_of('09_PANEL_REAR (2)') and abs(bbox_of('09_PANEL_REAR (2)')[2]-563)<0.5:
        zs=[]
        for o in list(root.allOccurrences):
            if o.component.name=='09_PANEL_REAR (2)':
                bb=o.boundingBox; zs.append((round(bb.minPoint.z*10,1),round(bb.maxPoint.z*10,1)))
        delete_named('09_PANEL_REAR (2)')
        for (z0,z1) in zs:
            occ=new_comp('09_PANEL_REAR'); c=occ.component
            box(c,110,1150,569,571,z0,z1,'new'); set_mat(c,'Plastic, Opaque White'); made.append('panel')
    return made

def step_C7_nozzle():
    made=[]
    if bbox_of('08_FILL_NOZZLE (1)') and abs(bbox_of('08_FILL_NOZZLE (1)')[4]-345)<0.5:
        for nm in ('08_FILL_NOZZLE (1)','08_TIER_DROP_X (1)','08_TIER_DROP_Y (1)','08_TIER_DROP_V1','08_TIER_DROP_V2','08_TIER_DROP_V3','08_TIER_DROP_V4'):
            delete_named(nm)
        for n,zb in enumerate((300,700,1100,1500)):
            zn = zb+85          # nozzle bottom (outlet) 38 mm above rim 347
            occ=new_comp('08_FILL_NOZZLE'); c=occ.component; box(c,140,160,490,510,zn,zn+45,'new'); set_mat(c,'PVC, Unplasticized')
            occ=new_comp('08_TIER_DROP_X'); c=occ.component; shs(c,70,150,492,508,zn+37,zn+53,2); set_mat(c,'PVC, Flexible')
            occ=new_comp('08_TIER_DROP_Y'); c=occ.component; shs(c,62,78,500,580,zn+37,zn+53,2); set_mat(c,'PVC, Flexible')
            made.append(n)
        # verticals from the manifold (Z 1000-1300) to each Y-run, no overlaps: tier1 422..1030, tier2 822..1100, tier3 1170..1222 (manifold above? tier 3 run at 1222 -> from 1222 up to 1240 solenoid), tier4 1300..1622
        segs={'08_TIER_DROP_V1':(438,1030),'08_TIER_DROP_V2':(838,1100),'08_TIER_DROP_V3':(1170,1238),'08_TIER_DROP_V4':(1300,1638)}
        for nm,(z0,z1) in segs.items():
            occ=new_comp(nm); c=occ.component; shs(c,62,78,572,588,z0,z1,2); set_mat(c,'PVC, Flexible'); made.append(nm)
    return made

def step_C8_header():
    made=[]
    if bbox_of('09_DRAIN_HEADER') and abs(bbox_of('09_DRAIN_HEADER')[0]-1216)<0.5:
        for nm in ('09_DRAIN_HEADER','09_HEADER_LEVEL_SW','09_TRAY_DRAIN_X (2)','09_OVF_X (2)','09_TUNDISH','10_LEAK_SENSOR'):
            delete_named(nm)
        occ=new_comp('09_DRAIN_HEADER'); c=occ.component; shs(c,1262,1312,455,505,200,1450,2.5); set_mat(c,'PVC, Flexible'); made.append('header')
        occ=new_comp('09_HEADER_LEVEL_SW'); c=occ.component; box(c,1267,1307,460,500,250,310,'new'); set_mat(c,'Polyethylene, High Density')
        for z0 in (190,590,990,1390):
            occ=new_comp('09_TRAY_DRAIN_X'); c=occ.component; shs(c,1156,1287,460,500,z0,z0+40,2.5); set_mat(c,'PVC, Flexible')
        for z0 in (144,544,944,1344):
            occ=new_comp('09_OVF_X'); c=occ.component; shs(c,1112,1267,464,496,z0,z0+32,2); set_mat(c,'PVC, Flexible')
        occ=new_comp('09_TUNDISH'); c=occ.component; box(c,1252,1312,425,545,20,100,'new'); box(c,1255,1309,428,542,23,101,'cut'); set_mat(c,'PVC, Flexible')
        occ=new_comp('10_LEAK_SENSOR'); c=occ.component; box(c,1226,1306,440,520,0,20,'new'); set_mat(c,'ABS Plastic')
        made.append('done')
    return made

def step_C9_C10_tray_deck():
    made=[]
    if '08_FLOOD_TRAY_F' not in names():
        delete_named('08_FLOOD_TRAY'); delete_named('09_OVF_COLLAR')
        for zb in (300,700,1100,1500):
            occ=new_comp('08_FLOOD_TRAY_F'); c=occ.component
            box(c,40,1216,0,560,zb,zb+47,'new')
            box(c,43,1213,3,557,zb+5.5,zb+48,'cut')           # cavity, flat floor top at +5.5 (front)
            # wedge: floor top falls 2.5 mm from front (Y 3) to rear (Y 557): triangle in YZ extruded along X
            pi=c.constructionPlanes.createInput(); pi.setByOffset(root.yZConstructionPlane, V(43*U)); pl=c.constructionPlanes.add(pi)
            sk=c.sketches.add(pl)
            pts=[P3(43*U,3*U,(zb+5.5)*U),P3(43*U,557*U,(zb+3)*U),P3(43*U,557*U,(zb+5.5)*U)]
            sp=[sk.modelToSketchSpace(p) for p in pts]
            for i in range(3): sk.sketchCurves.sketchLines.addByTwoPoints(sp[i],sp[(i+1)%3])
            inp=c.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
            inp.setDistanceExtent(False, V(1170*U))
            try: c.features.extrudeFeatures.add(inp)
            except:
                inp=c.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
                inp.setDistanceExtent(False, V(-1170*U)); c.features.extrudeFeatures.add(inp)
            # collar: ring OD 38 ID 32, 30 high above the local floor at (1096,480)
            pl2=plane_z(c, zb+3); sk2=c.sketches.add(pl2)
            cc=sk2.modelToSketchSpace(P3(1096*U,480*U,(zb+3)*U))
            sk2.sketchCurves.sketchCircles.addByCenterRadius(cc,19*U); sk2.sketchCurves.sketchCircles.addByCenterRadius(cc,16*U)
            ring=max([sk2.profiles.item(i) for i in range(sk2.profiles.count)], key=lambda p:p.areaProperties().area)
            # the ring profile is the annulus (area pi(19^2-16^2)=330) vs inner disc (804) -> pick the annulus explicitly
            for i in range(sk2.profiles.count):
                pr=sk2.profiles.item(i)
                if abs(pr.areaProperties().area - math.pi*(1.9**2-1.6**2))<0.05: ring=pr
            inp=c.features.extrudeFeatures.createInput(ring, adsk.fusion.FeatureOperations.JoinFeatureOperation)
            inp.setDistanceExtent(False, V(30*U))
            try: c.features.extrudeFeatures.add(inp)
            except:
                inp=c.features.extrudeFeatures.createInput(ring, adsk.fusion.FeatureOperations.JoinFeatureOperation); inp.setDistanceExtent(False, V(-30*U)); c.features.extrudeFeatures.add(inp)
            # floor openings
            cyl_cut(c,1156,480,zb-1,zb+8,40); cyl_cut(c,1096,480,zb-1,zb+8,32)
            set_mat(c,'Polyethylene, High Density'); made.append(zb)
    # deck panel clearance holes (shared component -> cut once)
    for o in root.allOccurrences:
        if o.component.name=='04_DECK_PANEL':
            c=o.component
            cyl=0
            for b in c.bRepBodies:
                for f in b.faces:
                    if f.geometry.surfaceType==adsk.core.SurfaceTypes.CylinderSurfaceType: cyl+=1
            if cyl<3:
                # local coords: panel is at its own origin? use occurrence transform inverse
                m=o.transform.copy(); m.invert()
                def loc(x,y,z):
                    p=P3(x*U,y*U,z*U); p.transformBy(m); return p
                bb=o.boundingBox; zb=bb.minPoint.z*10
                for (cx,dia) in ((1156,52),(1096,46)):
                    p=loc(cx,480,zb-1)
                    pl=c.constructionPlanes.createInput(); pl.setByOffset(c.xYConstructionPlane, V(p.z)); pln=c.constructionPlanes.add(pl)
                    sk=c.sketches.add(pln); cc=sk.modelToSketchSpace(p)
                    sk.sketchCurves.sketchCircles.addByCenterRadius(cc, dia/2*U)
                    inp=c.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
                    inp.setSymmetricExtent(V(10*U), True)
                    c.features.extrudeFeatures.add(inp)
                made.append('deck holes')
            break
    return made

def step_C11_anchor():
    made=[]
    if '14_ANCHOR_STRUT_106B' not in names():
        delete_named('14_WALL_ANCHOR')
        for (x0,x1) in ((0,60),(1216,1276)):
            occ=new_comp('14_ANCHOR_STRUT_106B'); c=occ.component
            cx=(x0+x1)/2
            box(c, x0,x1, 560,563, 1830,1930,'new')                       # rack plate 60x100x3 on the rear face
            shs(c, cx-15,cx+15, 563,663, 1865,1895, 1.5)                  # outer 30 SHS, 100 long (set for 127 mm stand-off)
            shs(c, cx-12.5,cx+12.5, 620,690, 1867.5,1892.5, 1.5)          # inner 25 SHS, telescoped
            box(c, cx-30,cx+30, 686,690, 1850,1910,'join')                 # wall foot 60x60x4
            set_mat(c,GI); made.append(cx)
    return made

def step_C12_C13_C14_feet_upright_saddles():
    made=[]
    if '13_FOOT_INSERT_108' not in names():
        for (x0,y0) in ((1.6,1.6),(1.6,521.6),(1217.6,1.6),(1217.6,521.6)):
            occ=new_comp('13_FOOT_INSERT_108'); c=occ.component
            box(c, x0,x0+36.8, y0,y0+36.8, 0,40,'new'); cyl_cut(c, x0+18.4,y0+18.4,-1,41,12); set_mat(c,'Steel'); made.append('insert')
    # upright drain holes: shared component; local Z 55, along the two hole-axis directions found on the body
    for o in root.allOccurrences:
        if o.component.name.startswith('02_UPRIGHT'):
            c=o.component; b=c.bRepBodies.item(0)
            small=[f for f in b.faces if f.geometry.surfaceType==adsk.core.SurfaceTypes.CylinderSurfaceType and abs(f.geometry.radius*10-3.0)<0.1]
            if not small:
                axes=set()
                for f in b.faces:
                    if f.geometry.surfaceType==adsk.core.SurfaceTypes.CylinderSurfaceType:
                        a=f.geometry.axis; axes.add((round(abs(a.x)),round(abs(a.y)),round(abs(a.z))))
                lb=b.boundingBox
                for ax in axes:
                    pl=c.constructionPlanes.createInput()
                    base = c.yZConstructionPlane if ax[0]==1 else c.xZConstructionPlane
                    pl.setByOffset(base, V(0)); pln=c.constructionPlanes.add(pl)
                    sk=c.sketches.add(pln)
                    cen=P3((lb.minPoint.x+lb.maxPoint.x)/2,(lb.minPoint.y+lb.maxPoint.y)/2, lb.minPoint.z+5.5)
                    sk.sketchCurves.sketchCircles.addByCenterRadius(sk.modelToSketchSpace(cen), 0.3)
                    inp=c.features.extrudeFeatures.createInput(sk.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
                    inp.setSymmetricExtent(V(5.0), True); c.features.extrudeFeatures.add(inp)
                made.append('upright drain holes')
            break
    if '06_LED_SADDLE_302' not in names():
        for zr in (623.4,1023.4,1423.4,1823.4):
            for y0 in (168,372):
                for (x0,x1) in ((40,42),(1214,1216)):
                    occ=new_comp('06_LED_SADDLE_302'); c=occ.component
                    box(c,x0,x1,y0-10,y0+30,zr-2,zr+30,'new'); set_mat(c,GI)
        made.append('saddles')
    return made

def step_C15_C16_panels_cabletray():
    made=[]
    for o in list(root.allOccurrences):
        if o.component.name=='11_CABLE_TRAY_TIER':
            bb=o.boundingBox
            if abs(bb.minPoint.y*10-515)<0.5:
                zs=[(round(bb.minPoint.z*10,1),round(bb.maxPoint.z*10,1))]
                o.deleteMe()
                for (z0,z1) in zs:
                    occ=new_comp('11_CABLE_TRAY_TIER'); c=occ.component; shs(c,110,1110,525,559,z0,z1,1.5); set_mat(c,'ABS Plastic'); made.append(z0)
    # right side panels tiers 2-4: notch 40x40 at the overflow lateral (Y 464-496, Z 544-576 etc.) -> cut via shared comp is wrong (left panels share). Recreate right panels as separate comps.
    if '09_PANEL_SIDE_R_NOTCHED' not in names():
        for o in list(root.allOccurrences):
            if o.component.name=='09_PANEL_SIDE (1)':
                bb=o.boundingBox
                if bb.minPoint.x*10>1000 and bb.minPoint.z*10>700:
                    z0,z1=round(bb.minPoint.z*10,1),round(bb.maxPoint.z*10,1); o.deleteMe()
                    occ=new_comp('09_PANEL_SIDE_R_NOTCHED'); c=occ.component
                    box(c,1212,1214,45,510,z0,z1,'new'); box(c,1211,1215,460,500,z0-1,z0+40,'cut'); set_mat(c,'Plastic, Opaque White'); made.append(z0)
    return made

def step_C17_params():
    up=des.userParameters; made=[]
    for nm,expr,cm in (('Brace_Len','1810 mm','ECP-01 EDR-018'),('Brace_Hole_Pitch','1780.1 mm','EDR-018'),('Anchor_Range_Min','90 mm','EDR-017'),('Anchor_Range_Max','320 mm','EDR-017'),('Nozzle_Outlet_Above_Rim','38 mm','ICR-005'),('Header_X','1262 mm','ICR-006'),('Rack_Width_Installed','1472 mm','ICR-006'),('Cross_Beams_Per_Tier','2','EDR-014')):
        if not up.itemByName(nm):
            up.add(nm, adsk.core.ValueInput.createByString(expr), '' if expr.replace(' ','').isdigit() else 'mm', cm); made.append(nm)
    return made

def step_C18_verify():
    ents=adsk.core.ObjectCollection.create()
    for o in root.allOccurrences: ents.add(o)
    inp=des.createInterferenceInput(ents); inp.areCoincidentFacesIncluded=False
    res=des.analyzeInterference(inp)
    pairs={}
    for r in res:
        def nm(b):
            try: return b.assemblyContext.component.name
            except: return b.parentComponent.name
        k=tuple(sorted((nm(r.entityOne),nm(r.entityTwo)))); pairs[k]=pairs.get(k,0)+1
    pp=root.physicalProperties; bb=root.boundingBox; cg=pp.centerOfMass
    return {'parts':len(names()),'occ':root.allOccurrences.count,'mass':round(pp.mass,3),'cg':[round(cg.x*10,1),round(cg.y*10,1),round(cg.z*10,1)],
            'bbox':[round(bb.minPoint.x*10,1),round(bb.maxPoint.x*10,1),round(bb.minPoint.y*10,1),round(bb.maxPoint.y*10,1),round(bb.minPoint.z*10,1),round(bb.maxPoint.z*10,1)],
            'interference_pairs':{f'{a} x {b}':n for (a,b),n in sorted(pairs.items())}}

def run_step(fn):
    try:
        r=fn(); print(json.dumps({'step':fn.__name__,'ok':True,'result':r}))
    except Exception:
        print(json.dumps({'step':fn.__name__,'ok':False,'trace':traceback.format_exc()}))
