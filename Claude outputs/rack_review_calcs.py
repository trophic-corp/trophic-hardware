"""Independent engineering verification calculations for RK-A rack (review only).
All units N, mm, MPa unless stated. Geometry from Fusion CEA_RACK_INTEGRATED_v2 v8 (read 2026-09-10).
"""
import numpy as np, math, json

E = 200_000.0   # MPa steel
G = 77_000.0
g = 9.81
fy = 210.0      # YST210

def shs(b, t):
    """Square hollow section props (sharp corners) -> A, I, Z, J"""
    A = b*b - (b-2*t)**2
    I = (b**4 - (b-2*t)**4)/12
    Z = I/(b/2)
    am = (b-t)**2          # enclosed area at mid-thickness
    J = 4*am**2*t/(4*(b-t))
    return A, I, Z, J

res = {}
# ---------- sections ----------
Ap, Ip, Zp, Jp = shs(40, 1.6)
Ab, Ib, Zb, Jb = shs(30, 1.5)
Ar, Ir, Zr, Jr = shs(25, 1.5)
res['sections'] = dict(post=dict(A=Ap, I=Ip, Z=Zp), beam=dict(A=Ab, I=Ib, Z=Zb), rail=dict(A=Ar, I=Ir, Z=Zr))

# ---------- A. Long beam bending / deflection (two beams share tier load) ----------
L = 1176.0
def beam_case(mass_kg, I=Ib, Z=Zb):
    w = mass_kg*g/2/L          # N/mm per beam
    d = 5*w*L**4/(384*E*I)
    M = w*L**2/8
    s = M/Z
    return dict(load_kg=mass_kg, deflection_mm=round(d,3), stress_MPa=round(s,1), SF_yield=round(fy/s,1))
res['beam'] = {
    'beam_only': [beam_case(m) for m in (22.5, 31.3, 38.0, 80.0)],
    'beam_plus_rail_noncomposite': [beam_case(m, I=Ib+Ir, Z=(Ib+Ir)/15) for m in (22.5, 38.0, 80.0)],
}

# ---------- B. Deck cross rail (25x25x1.5, span 510 between long rails, 3 bays, 4 rails) ----------
# Tier load through mesh onto 4 cross rails; interior rails take ~1/3 each of tributary width ~392
Lr = 510.0
for m in (38.0, 80.0):
    w = (m*g/3)/Lr   # interior rail tributary 1/3 of tier load
    d = 5*w*Lr**4/(384*E*Ir)
    M = w*Lr**2/8
    res.setdefault('cross_rail',[]).append(dict(load_kg=m, deflection_mm=round(d,3), stress_MPa=round(M/Zr,1)))

# ---------- C. Upright compression / buckling ----------
dry = 112.66
tier_service, tier_rated = 38.0, 80.0
for name, m in (('service_38kg_tier', dry+4*tier_service), ('rated_80kg_tier', dry+4*tier_rated)):
    P = m*g/4
    sig = P/Ap
    out = dict(total_kg=m, P_per_post_N=round(P,0), stress_MPa=round(sig,2))
    for Kl in (400, 1950, 2*1950, 2*1800):
        Pcr = math.pi**2*E*Ip/Kl**2
        out[f'Pcr_Le{Kl}_N'] = round(Pcr,0)
        out[f'SF_Le{Kl}'] = round(Pcr/P,1)
    res.setdefault('upright',{})[name]=out

# ---------- D. Tip-over (rigid body), CG from Fusion: X 640.7, Y 357.3, Z 930.4 (dry) ----------
# feet centres at post centres: Y 20 and 540 ; X 20 and 1236
def tip(mass, cgY, cgZ, h_push=1500.0):
    fwd = mass*g*(cgY-20)/h_push     # push toward front (rotate about front feet) -> arm from front foot line
    bwd = mass*g*(540-cgY)/h_push    # push toward rear (rotate about rear feet)
    side = mass*g*(640.7-20)/h_push
    return dict(mass_kg=round(mass,1), cgY=round(cgY,0), cgZ=round(cgZ,0),
                push_to_rear_tips_at_N=round(bwd,0), push_to_front_tips_at_N=round(fwd,0), push_sideways_tips_at_N=round(side,0))
res['tipover'] = {}
res['tipover']['dry_model_112.66kg'] = tip(112.66, 357.3, 930.4)
# structure-only ~62 kg (assume CG at Y 280 centre, Z ~ 900)
res['tipover']['structure_only_62kg'] = tip(62.0, 280.0, 900.0)
# loaded: + 4 trays x 38 kg at Y 280, Z = bed+~20 (300,700,1100,1500)
m_tr = 4*38.0
cgY = (112.66*357.3 + m_tr*280)/(112.66+m_tr)
cgZ = (112.66*930.4 + 38*(320+720+1120+1520))/(112.66+m_tr)
res['tipover']['loaded_38kg_tier'] = tip(112.66+m_tr, cgY, cgZ)
# loaded with LED fixtures at spec max 4 kg each (model has 1.23 kg): +8*(4-1.23)=22.2 kg at Y ~280, Z ~ 1200 avg
m_led = 8*(4.0-1.227)
cgY2 = (112.66*357.3 + m_tr*280 + m_led*280)/(112.66+m_tr+m_led)
cgZ2 = (112.66*930.4 + 38*(320+720+1120+1520) + m_led*1200)/(112.66+m_tr+m_led)
res['tipover']['loaded_38kg_tier_LED4kg'] = tip(112.66+m_tr+m_led, cgY2, cgZ2)
# top tier only loaded (asymmetric, worst for tipping) empty otherwise; top tray pulled 200 mm forward
m_top = 38.0
cgY3 = (112.66*357.3 + m_top*(280-200))/(112.66+m_top)
cgZ3 = (112.66*930.4 + m_top*1520)/(112.66+m_top)
res['tipover']['top_tier_only_tray_pulled_200mm'] = tip(112.66+m_top, cgY3, cgZ3)

# ---------- E. Depth-plane sway: 2D frame, 4 posts share equally -> analyse one YZ frame (2 posts + base short beam) ----------
# Simple model: two posts (pinned at feet) joined by base beam at Z=165 (semi-rigid springs k), and
# 4 tier levels where front and rear beams are connected through deck frame (treated as rigid link with semi-rigid
# rotational springs k at each post). Horizontal load H at Z=1500 (top bed) on this half-frame = F/2.
def frame_sway(F_total, k_joint):  # k_joint in N.mm/rad, per joint
    # nodes: post nodes at z levels
    zl = [0.0, 165.0, 258.4, 658.4, 1058.4, 1458.4, 1500.0, 1950.0]
    nz = len(zl)
    # DOF per node: u (Y-transl), w (Z-transl), theta
    # posts: front (y=20) and rear (y=540) -> node ids: front i, rear nz+i
    N = 2*nz
    # link members at levels 1..5 (base + 4 tiers) with semi-rigid ends
    # implement: beam element between front node i and rear node i with end springs -> use element with
    # rotational springs via condensation: effective stiffness of semi-rigid beam (Monforton & Wu)
    def beam_k(EI, EA, Lm, k1, k2):
        # semi-rigid end fixity factors
        r1 = 1.0/(1+3*EI/(k1*Lm)) if k1 < 1e15 else 1.0
        r2 = 1.0/(1+3*EI/(k2*Lm)) if k2 < 1e15 else 1.0
        den = 4 - r1*r2
        # modified stiffness matrix (local: u1,v1,t1,u2,v2,t2) axial + bending
        k = np.zeros((6,6))
        k[0,0]=k[3,3]=EA/Lm; k[0,3]=k[3,0]=-EA/Lm
        a = EI/Lm**3
        c11 = 12*a*(r1+r2+r1*r2)/den
        c12 = 6*a*Lm*r1*(2+r2)/den
        c13 = 6*a*Lm*r2*(2+r1)/den
        c22 = 12*a*Lm**2*r1/den
        c23 = 6*a*Lm**2*r1*r2/den
        c33 = 12*a*Lm**2*r2/den
        k[1,1]=c11; k[1,2]=c12; k[1,4]=-c11; k[1,5]=c13
        k[2,1]=c12; k[2,2]=c22; k[2,4]=-c12; k[2,5]=c23
        k[4,1]=-c11; k[4,2]=-c12; k[4,4]=c11; k[4,5]=-c13
        k[5,1]=c13; k[5,2]=c23; k[5,4]=-c13; k[5,5]=c33
        return k
    def T(cx, cy):
        t = np.zeros((6,6))
        t[0,0]=cx; t[0,1]=cy; t[1,0]=-cy; t[1,1]=cx; t[2,2]=1
        t[3,3]=cx; t[3,4]=cy; t[4,3]=-cy; t[4,4]=cx; t[5,5]=1
        return t
    K = np.zeros((3*N,3*N))
    def add(el, k):
        idx = [3*el[0],3*el[0]+1,3*el[0]+2,3*el[1],3*el[1]+1,3*el[1]+2]
        for a_ in range(6):
            for b_ in range(6):
                K[idx[a_],idx[b_]] += k[a_,b_]
    # posts (rigid joints along the continuous post) - member axis along Z: local x = global Z
    for side in (0, nz):
        for i in range(nz-1):
            Lm = zl[i+1]-zl[i]
            kl = beam_k(E*Ip, E*Ap, Lm, 1e30, 1e30)
            t = T(0.0, 1.0)   # local x along +Z : cx = cos(angle between local x and global Y)=0, cy=1
            add((side+i, side+i+1), t.T@kl@t)
    # base beam (30x30x1.5 short beam, Y-span 520 between post centres) at level index 1, springs k_joint
    Lm = 520.0
    kl = beam_k(E*Ib, E*Ab, Lm, k_joint, k_joint)
    add((1, nz+1), kl)
    # tier levels: deck frame (2 long rails + 4 cross rails 25x25) acting as link between front & rear beams,
    # with joint springs (beam-to-post bracket rotation about X) at each end. Use cross-rail bending stiffness x4/4 posts -> per frame 2 rails
    for i in (2,3,4,5):
        kl = beam_k(E*(2*Ir), E*(2*Ar), Lm, k_joint, k_joint)
        add((i, nz+i), kl)
    # supports: feet pinned (u,w fixed) at node 0 and nz
    fixed = [0,1, 3*nz, 3*nz+1]
    F = np.zeros(3*N)
    F[3*6] = F_total/2/2   # load at Z=1500 node on front post ; half frame gets F/2, split to both posts
    F[3*(nz+6)] = F_total/2/2
    free = [d for d in range(3*N) if d not in fixed]
    Kf = K[np.ix_(free,free)]
    try:
        u = np.linalg.solve(Kf, F[free])
    except np.linalg.LinAlgError:
        return float('inf')
    U = np.zeros(3*N); U[free]=u
    return U[3*6]   # sway at Z=1500
res['depth_plane_sway_mm'] = {}
for kj in (1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e30):
    res['depth_plane_sway_mm'][f'k_joint_{kj:.0e}_Nmm_per_rad'] = {
        '200N': round(frame_sway(200.0, kj),1), '300N': round(frame_sway(300.0, kj),1)}
# reference: 4 fully fixed cantilever posts from base beam level 165
for H in (200,300):
    d = H*(1500-165)**3/(3*E*Ip*4)
    res['depth_plane_sway_mm'][f'ref_4_fixed_base_cantilevers_{H}N'] = round(d,1)

# ---------- F. Width-plane sway with X brace (tension diagonal 25x3, 1771.6 long, angle 48.4 deg) ----------
Abr = 25*3
Lbr = 1771.6
th = math.atan2(1325,1176)
for H in (200,300):
    # single tension diagonal carries H/cos(th); brace elongation -> sway
    Fb = H/math.cos(th)
    dl = Fb*Lbr/(E*Abr)
    sway = dl/math.cos(th)
    res.setdefault('width_plane_brace',{})[f'{H}N'] = dict(brace_force_N=round(Fb,0), brace_stress_MPa=round(Fb/Abr,2), sway_at_brace_top_mm=round(sway,3),
        bolt_bearing_on_3mm_flat_MPa=round(Fb/(8*3),1), bolt_shear_MPa=round(Fb/(math.pi*16),1))
# bolt-hole clearance slip: 1 mm clearance at each end -> up to 2 mm along brace -> sway
res['width_plane_brace']['hole_clearance_slip_sway_mm'] = round(2.0/math.cos(th),2)

# ---------- G. Bolt preload vs tube wall (M8 A2-70 at 18 N.m through 40x40x1.6 both walls) ----------
Tq = 18_000.0  # N.mm
Fp = Tq/(0.2*8)
res['bolt_preload_N'] = round(Fp,0)
# wall as plate strip spanning 36.8 between side walls, point load at centre, effective width ~ 3*t+nut ~ 20 mm
b_eff = 20.0; t = 1.6; span = 36.8
M = Fp*span/8   # fixed-ended strip
sig = M/(b_eff*t**2/6)
res['tube_wall_bending_under_preload_MPa'] = round(sig,0)
# preload at which wall strip yields (plastic hinge at ends+mid):
Mp = fy*b_eff*t**2/4
F_yield = 8*Mp/span
res['preload_at_wall_collapse_N'] = round(F_yield,0)
res['torque_for_that_preload_Nm'] = round(F_yield*0.2*8/1000,2)
# same for 30x30x1.5 and 25x25x1.5
for b,t in ((30,1.5),(25,1.5)):
    span=b-2*t; Mp=fy*b_eff*t**2/4; Fy=8*Mp/span
    res[f'preload_at_wall_collapse_{b}x{b}x{t}_N']=round(Fy,0)

# ---------- H. Overflow collar (weir) capacity, DN32 crest ----------
Cd=0.6
for D in (25,32,40):
    per = math.pi*D/1000
    out={}
    for h in (5,8,10,15,17):
        Q = (2/3)*Cd*math.sqrt(2*g)*per*(h/1000)**1.5   # m3/s
        out[f'h{h}mm_Lpm']=round(Q*60000,1)
    # head needed for 7.2 L/min
    h_req = ((7.2/60000)/((2/3)*Cd*math.sqrt(2*g)*per))**(2/3)*1000
    out['head_for_7.2Lpm_mm']=round(h_req,1)
    res.setdefault('overflow_weir',{})[f'DN{D}']=out

# ---------- I. Tray drain orifice DN40 at 22 mm head; solenoid Kv effect ----------
A40 = math.pi/4*0.04**2
Q = 0.62*A40*math.sqrt(2*g*0.022)
res['drain_orifice_DN40_22mm_Lpm'] = round(Q*60000,1)
for Kv in (10, 20, 30, 50):   # m3/h at 1 bar
    Qm3h = 30.7/1000*60
    dp_bar = (Qm3h/Kv)**2
    res.setdefault('drain_valve_dp_mm_water_at_30.7Lpm',{})[f'Kv{Kv}'] = round(dp_bar*10197,0)
# gravity available: 22 mm tray head + ~100 mm fall to solenoid (Z 300 -> 215)
res['drain_available_head_mm'] = 22+ (300-215)

# ---------- J. Seismic per IS 1893 Pt1 2016 cl 7.13 (non-structural) ----------
for Z_ in (0.10, 0.16):
    for ap,Rp,lab in ((1.0,2.5,'rigid'),(2.5,2.5,'flexible')):
        coef = (Z_/2)*(1+0)*(ap/Rp)*1.0
        m = 112.66+4*38
        cgz = res['tipover']['loaded_38kg_tier']['cgZ']
        Mo = coef*m*g*cgz/1000
        Mr = m*g*(540-res['tipover']['loaded_38kg_tier']['cgY'])/1000
        res.setdefault('seismic',{})[f'Z{Z_}_{lab}'] = dict(coef=round(coef,3), overturning_Nm=round(Mo,0), restoring_rear_Nm=round(Mr,0), SF=round(Mr/Mo,1))

# ---------- K. Foot pressure ----------
P = (112.66+4*38)*g/4
res['foot'] = dict(load_per_foot_N=round(P,0), pressure_on_dia50_kPa=round(P/(math.pi*25**2)*1000,0), pressure_on_100x100_pad_kPa=round(P/10000*1000,0))

# ---------- L. LED rail 20x20x1.5 Al, fixture 2 and 4 kg on 2 hangers at 876 centres ----------
Ial = (20**4-17**4)/12
for mfix in (2.0,4.0):
    Pp = mfix*g/2
    a = 150.0; Lr_=1176.0
    d = Pp*a*(3*Lr_**2-4*a**2)/(24*69000*Ial)
    res.setdefault('led_rail',{})[f'{mfix}kg'] = round(d,2)

# ---------- M. Brace geometry from model ----------
res['brace_geometry'] = dict(model_bar_centreline_length_mm=round(math.hypot(1176,1325),1), drawing_length_mm=1797,
    bbox_diagonal_mm=round(math.hypot(1194.8,1341.6),1),
    grid_compatible_hole_centres=dict(dZ1250=round(math.hypot(1216,1250),1), dZ1300=round(math.hypot(1216,1300),1)),
    drawing_hole_centres=1757, dZ_implied_by_1757=round(math.sqrt(1757**2-1216**2),1))

# ---------- N. Fan vibration: beam first mode ----------
mu = (80/2+1.58)/1.176   # kg/m
EI = E*1e6*Ib*1e-12
f1 = (math.pi/(2*1.176**2))*math.sqrt(EI/mu)
res['beam_first_mode_Hz_80kg'] = round(f1,1)

print(json.dumps(res, indent=1))
