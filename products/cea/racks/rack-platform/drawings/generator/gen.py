import math, html

W,H = 1660, 1180
M   = 46
# view regions (first angle): FRONT tl, END tr, TOP bl, ISO br
REG = {
 'FRONT': (100,  96, 700, 430),
 'END'  : (890,  96, 660, 430),
 'TOP'  : (100, 620, 700, 430),
 'ISO'  : (890, 620, 660, 430),
}
C_OUT='var(--line)'; C_HID='var(--hidden)'; C_DIM='var(--dim)'; C_FILL='var(--face)'
C_ACC='var(--acc)'; C_CTR='var(--ctr)'

def esc(s): return html.escape(str(s))

def fit(w,h,region,pad=64):
    x,y,rw,rh = region
    if w<=0 or h<=0: return 1.0
    return min((rw-2*pad)/w, (rh-2*pad)/h)

def centre(w,h,region):
    x,y,rw,rh = region
    return x+(rw-w)/2, y+(rh-h)/2

def dim_h(x1,x2,y,txt,uid,flip=False,off=0):
    """horizontal dimension"""
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{C_DIM}" stroke-width="1.4" '
            f'marker-start="url(#a2{uid})" marker-end="url(#a1{uid})"/>'
            f'<line x1="{x1}" y1="{y-6}" x2="{x1}" y2="{y+6}" stroke="{C_DIM}" stroke-width="1.4"/>'
            f'<line x1="{x2}" y1="{y-6}" x2="{x2}" y2="{y+6}" stroke="{C_DIM}" stroke-width="1.4"/>'
            f'<text x="{(x1+x2)/2}" y="{y-9+off}" fill="{C_DIM}" font-size="19" text-anchor="middle">{esc(txt)}</text>')

def dim_v(y1,y2,x,txt,uid):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{C_DIM}" stroke-width="1.4" '
            f'marker-start="url(#a2{uid})" marker-end="url(#a1{uid})"/>'
            f'<line x1="{x-6}" y1="{y1}" x2="{x+6}" y2="{y1}" stroke="{C_DIM}" stroke-width="1.4"/>'
            f'<line x1="{x-6}" y1="{y2}" x2="{x+6}" y2="{y2}" stroke="{C_DIM}" stroke-width="1.4"/>'
            f'<text x="{x-10}" y="{(y1+y2)/2+6}" fill="{C_DIM}" font-size="19" text-anchor="end">{esc(txt)}</text>')

def label(region,txt,sub=''):
    x,y,rw,rh = region
    s=f'<text x="{x}" y="{y-14}" fill="{C_ACC}" font-size="21" font-weight="600" letter-spacing="1.5">{esc(txt)}</text>'
    if sub: s+=f'<text x="{x+len(txt)*13+22}" y="{y-14}" fill="var(--ink3)" font-size="17">{esc(sub)}</text>'
    return s

def frame(region):
    x,y,rw,rh=region
    return (f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" fill="var(--vp)" '
            f'stroke="var(--vpline)" stroke-width="1" stroke-dasharray="6 7"/>')

def zig(x,y0,y1,uid):
    """vertical break zigzag"""
    m=(y0+y1)/2; w=13
    return (f'<path d="M{x} {y0} L{x} {m-26} L{x-w} {m-9} L{x+w} {m+9} L{x} {m+26} L{x} {y1}" '
            f'fill="none" stroke="{C_OUT}" stroke-width="1.6"/>')

# ---------- view builders ----------
def tube_long(part,uid):
    """SHS, broken view. Scale is driven by a target bar height so the view always fits its region."""
    L=part['L']; A=part['A']; t=part['t']; hl=part.get('holes')
    out={}; TH=48.0; GAP=58.0; pad=76
    def layout(region):
        s=TH/A
        avail=region[2]-2*pad
        if L*s<=avail:
            return s, (L,0.0), False, L*s
        usable=avail-GAP
        segL=min(usable*0.66/s, L*0.55)      # asymmetric break: long left run shows the grid
        segR=min(usable*0.34/s, L*0.30)
        return s, (segL,segR), True, (segL+segR)*s+GAP
    def bar(region,title,sub,face2=False):
        s,segs,brk,wpx=layout(region)
        segL,segR=segs
        hpx=A*s
        ox,oy=centre(wpx,hpx,region)
        g=[frame(region), label(region,title,sub)]
        spans=[(ox,segL*s),(ox+segL*s+GAP,segR*s)] if brk else [(ox,L*s)]
        wt=max(t*s,2.0)
        for x0,ln in spans:
            g.append(f'<rect x="{x0:.1f}" y="{oy:.1f}" width="{ln:.1f}" height="{hpx:.1f}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.2"/>')
            if not face2:
                g.append(f'<line x1="{x0:.1f}" y1="{oy+wt:.1f}" x2="{x0+ln:.1f}" y2="{oy+wt:.1f}" stroke="{C_HID}" stroke-width="1.2" stroke-dasharray="9 6"/>')
                g.append(f'<line x1="{x0:.1f}" y1="{oy+hpx-wt:.1f}" x2="{x0+ln:.1f}" y2="{oy+hpx-wt:.1f}" stroke="{C_HID}" stroke-width="1.2" stroke-dasharray="9 6"/>')
        if brk: g.append(zig(ox+segL*s+GAP/2,oy-9,oy+hpx+9,uid))
        g.append(f'<line x1="{ox-20:.1f}" y1="{oy+hpx/2:.1f}" x2="{ox+wpx+20:.1f}" y2="{oy+hpx/2:.1f}" stroke="{C_CTR}" stroke-width="1" stroke-dasharray="22 6 4 6"/>')
        return g,s,segL,segR,brk,wpx,ox,oy,hpx
    # ---- FRONT
    r=REG['FRONT']
    _s0,_sg0,brk0,_w0=layout(r)
    g,s,segL,segR,brk,wpx,ox,oy,hpx=bar(r,'FRONT VIEW','broken · true length %d'%L if brk0 else 'full length')
    if hl:
        n=0; x=hl['start']
        while x<=segL+1e-6 and n<18:
            g.append(f'<circle cx="{ox+x*s:.1f}" cy="{oy+hpx/2:.1f}" r="{max(hl["dia"]*s/2,3.4):.1f}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.5"/>')
            x+=hl['pitch']; n+=1
        if brk:
            xr=ox+segL*s+GAP; last=hl['start']+(hl['count']-1)*hl['pitch']
            k=0; back=0.0
            while back<=segR+1e-6 and k<12:
                g.append(f'<circle cx="{xr+(segR-back)*s:.1f}" cy="{oy+hpx/2:.1f}" r="{max(hl["dia"]*s/2,3.4):.1f}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.5"/>')
                back+=hl['pitch']; k+=1
            g.append(f'<text x="{xr+segR*s:.1f}" y="{oy-20:.1f}" fill="{C_DIM}" font-size="17" text-anchor="end">LAST HOLE {last}</text>')
        g.append(dim_h(ox,ox+hl['start']*s,oy+hpx+42,'%d'%hl['start'],uid))
        if n>1:
            g.append(dim_h(ox+hl['start']*s,ox+(hl['start']+hl['pitch'])*s,oy+hpx+76,'%d'%hl['pitch'],uid))
        g.append(f'<text x="{ox:.1f}" y="{oy-20:.1f}" fill="{C_DIM}" font-size="18">{hl["count"]} × ⌀{hl["dia"]} @ {hl["pitch"]} PITCH · {hl["faces"]} FACE(S)</text>')
    g.append(dim_h(ox,ox+wpx,oy+hpx+112,'%d OVERALL'%L,uid))
    g.append(dim_v(oy,oy+hpx,ox-26,'%d'%A,uid))
    out['FRONT']=''.join(g)
    # ---- TOP
    r=REG['TOP']
    g,s2,segL2,segR2,brk2,w2,ox2,oy2,hp2=bar(r,'TOP VIEW','second face' if hl else '',face2=True)
    if hl:
        n=0; x=hl['start']
        while x<=segL2+1e-6 and n<18:
            g.append(f'<circle cx="{ox2+x*s2:.1f}" cy="{oy2+hp2/2:.1f}" r="{max(hl["dia"]*s2/2,3.4):.1f}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.5"/>')
            x+=hl['pitch']; n+=1
        if brk2:
            xr2=ox2+segL2*s2+GAP; back=0.0; k=0
            while back<=segR2+1e-6 and k<12:
                g.append(f'<circle cx="{xr2+(segR2-back)*s2:.1f}" cy="{oy2+hp2/2:.1f}" r="{max(hl["dia"]*s2/2,3.4):.1f}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.5"/>')
                back+=hl['pitch']; k+=1
        g.append(f'<text x="{ox2:.1f}" y="{oy2-20:.1f}" fill="{C_DIM}" font-size="18">GRID REPEATS ON ADJACENT FACE · HOLES IN LINE</text>')
    g.append(dim_v(oy2,oy2+hp2,ox2-26,'%d'%A,uid))
    out['TOP']=''.join(g)
    # ---- END
    r=REG['END']; s3=fit(A,A,r,90); sp=A*s3
    ox3,oy3=centre(sp,sp,r); wt3=max(t*s3,2.5)
    e=[frame(r), label(r,'END VIEW','section')]
    e.append(f'<rect x="{ox3:.1f}" y="{oy3:.1f}" width="{sp:.1f}" height="{sp:.1f}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.4"/>')
    e.append(f'<rect x="{ox3+wt3:.1f}" y="{oy3+wt3:.1f}" width="{sp-2*wt3:.1f}" height="{sp-2*wt3:.1f}" fill="var(--vp)" stroke="{C_OUT}" stroke-width="1.8"/>')
    e.append(f'<line x1="{ox3-24:.1f}" y1="{oy3+sp/2:.1f}" x2="{ox3+sp+24:.1f}" y2="{oy3+sp/2:.1f}" stroke="{C_CTR}" stroke-width="1" stroke-dasharray="20 5 3 5"/>')
    e.append(f'<line x1="{ox3+sp/2:.1f}" y1="{oy3-24:.1f}" x2="{ox3+sp/2:.1f}" y2="{oy3+sp+24:.1f}" stroke="{C_CTR}" stroke-width="1" stroke-dasharray="20 5 3 5"/>')
    if hl:
        e.append(f'<circle cx="{ox3+sp/2:.1f}" cy="{oy3+sp/2:.1f}" r="{max(hl["dia"]*s3/2,4):.1f}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.4"/>')
    e.append(dim_h(ox3,ox3+sp,oy3+sp+52,'%d'%A,uid))
    e.append(dim_v(oy3,oy3+sp,ox3-30,'%d'%A,uid))
    e.append(f'<text x="{ox3+sp/2:.1f}" y="{oy3+sp+96:.1f}" fill="{C_DIM}" font-size="19" text-anchor="middle">WALL {t}</text>')
    out['END']=''.join(e)
    out['ISO']=iso_box(REG['ISO'],L,A,A,uid,broken=True,label_txt='ISOMETRIC')
    return out

def plate_views(part,uid):
    L=part['L']; Wd=part['W']; T=part['t']; uid=uid
    hl=part.get('holes'); out={}
    brk = L/max(Wd,1) > 6
    # FRONT = L x T (edge)
    r=REG['FRONT']; pad=76
    s=fit(L,max(T,8),r,pad); s=min(s,(r[3]-2*pad)/max(T*6,30))
    s=fit(L,Wd,r,pad)
    tp=max(T*s,4)
    ox,oy=centre(L*s,tp,r)
    b=[frame(r), label(r,'FRONT VIEW','edge · thickness %g'%T)]
    b.append(f'<rect x="{ox}" y="{oy}" width="{L*s}" height="{tp}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.2"/>')
    b.append(dim_h(ox,ox+L*s,oy+tp+56,'%d'%L,uid))
    b.append(f'<text x="{ox+L*s+26}" y="{oy+tp/2+7}" fill="{C_DIM}" font-size="19">t {T}</text>')
    out['FRONT']=''.join(b)
    # TOP = L x W (the real face)
    r=REG['TOP']; s=fit(L,Wd,r,76)
    ox,oy=centre(L*s,Wd*s,r)
    t2=[frame(r), label(r,'PLAN VIEW','developed face')]
    t2.append(f'<rect x="{ox}" y="{oy}" width="{L*s}" height="{Wd*s}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.4"/>')
    if hl:
        for (hx,hy) in hl['pos']:
            t2.append(f'<circle cx="{ox+hx*s}" cy="{oy+hy*s}" r="{max(hl["dia"]*s/2,3.4)}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="1.5"/>')
        t2.append(f'<text x="{ox}" y="{oy-20}" fill="{C_DIM}" font-size="18">{len(hl["pos"])} × ⌀{hl["dia"]}</text>')
    if part.get('perf'):
        step=max(Wd*s/6,14)
        yy=oy+step
        while yy<oy+Wd*s-6:
            xx=ox+step
            while xx<ox+L*s-6:
                t2.append(f'<circle cx="{xx}" cy="{yy}" r="2.6" fill="var(--hole)"/>')
                xx+=step
            yy+=step
    t2.append(dim_h(ox,ox+L*s,oy+Wd*s+62,'%d'%L,uid))
    t2.append(dim_v(oy,oy+Wd*s,ox-30,'%d'%Wd,uid))
    out['TOP']=''.join(t2)
    # END = W x T
    r=REG['END']; s=fit(Wd,max(T,10),r,86); s=min(s,(r[2]-172)/Wd)
    tp2=max(T*s,5); ox,oy=centre(Wd*s,tp2,r)
    e=[frame(r), label(r,'END VIEW','')]
    e.append(f'<rect x="{ox}" y="{oy}" width="{Wd*s}" height="{tp2}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.2"/>')
    e.append(dim_h(ox,ox+Wd*s,oy+tp2+56,'%d'%Wd,uid))
    e.append(f'<text x="{ox+Wd*s+26}" y="{oy+tp2/2+7}" fill="{C_DIM}" font-size="19">t {T}</text>')
    out['END']=''.join(e)
    out['ISO']=iso_box(REG['ISO'],L,Wd,max(T,6),uid,label_txt='ISOMETRIC')
    return out

def tray_views(part,uid):
    L=part['L']; Wd=part['W']; Hh=part['H']; T=part['t']; out={}
    bossy = part.get('boss_y', Wd/2.0)
    ovfx  = part.get('ovf_x', None)
    ovfd  = part.get('ovf_dia', 32)
    colh  = part.get('collar_h', 30)
    wt=max(T*3,3)

    # ---------- FRONT: section through the rim, showing the moulded collar ----------
    r=REG['FRONT']; s=fit(L,Hh*3,r,80)
    ox,oy=centre(L*s,Hh*s,r)
    hp=max(Hh*s,40); wt=max(T*s,3)
    b=[frame(r), label(r,'FRONT VIEW','section on the boss centreline')]
    b.append(f'<rect x="{ox}" y="{oy}" width="{L*s}" height="{hp}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.4"/>')
    b.append(f'<rect x="{ox+wt}" y="{oy}" width="{L*s-2*wt}" height="{hp-wt}" fill="var(--vp)" stroke="{C_HID}" stroke-width="1.4" stroke-dasharray="9 6"/>')
    floor=oy+hp-wt
    fl=hp*(part['flood']/Hh)
    b.append(f'<line x1="{ox+wt}" y1="{floor-fl}" x2="{ox+L*s-wt}" y2="{floor-fl}" stroke="{C_ACC}" stroke-width="2" stroke-dasharray="14 7"/>')
    b.append(f'<text x="{ox+L*s*0.30}" y="{floor-fl-11}" fill="{C_ACC}" font-size="18" text-anchor="middle">WORKING FLOOD {part["flood"]}</text>')
    if ovfx:
        cx=ox+(L-ovfx)*s; cw=max(ovfd*s,8); ch=hp*(colh/Hh)
        b.append(f'<rect x="{cx-cw/2-3}" y="{floor-ch}" width="{cw+6}" height="{ch}" fill="none" stroke="{C_OUT}" stroke-width="2.2"/>')
        b.append(f'<line x1="{cx-cw/2}" y1="{floor-ch}" x2="{cx-cw/2}" y2="{floor}" stroke="{C_HID}" stroke-width="1.3" stroke-dasharray="7 5"/>')
        b.append(f'<line x1="{cx+cw/2}" y1="{floor-ch}" x2="{cx+cw/2}" y2="{floor}" stroke="{C_HID}" stroke-width="1.3" stroke-dasharray="7 5"/>')
        b.append(f'<line x1="{cx}" y1="{floor-ch}" x2="{cx-46}" y2="{floor-ch-58}" stroke="{C_DIM}" stroke-width="1.2"/>')
        b.append(f'<text x="{cx-50}" y="{floor-ch-84}" fill="{C_DIM}" font-size="18" text-anchor="end">MOULDED OVERFLOW COLLAR</text>')
        b.append(f'<text x="{cx-50}" y="{floor-ch-62}" fill="{C_DIM}" font-size="18" text-anchor="end">CREST {colh} · BORE ⌀{ovfd}</text>')
        b.append(dim_v(floor-ch,floor,cx+cw/2+34,'%d'%colh,uid))
    dxc=ox+(L-part['drain_x'])*s; dw=max(part['drain']*s,8)
    b.append(f'<line x1="{dxc-dw/2}" y1="{floor}" x2="{dxc-dw/2}" y2="{floor+wt}" stroke="{C_OUT}" stroke-width="2"/>')
    b.append(f'<line x1="{dxc+dw/2}" y1="{floor}" x2="{dxc+dw/2}" y2="{floor+wt}" stroke="{C_OUT}" stroke-width="2"/>')
    b.append(f'<line x1="{dxc}" y1="{floor+wt}" x2="{dxc-40}" y2="{floor+wt+42}" stroke="{C_DIM}" stroke-width="1.2"/>')
    b.append(f'<text x="{dxc-44}" y="{floor+wt+46}" fill="{C_DIM}" font-size="18" text-anchor="end">⌀{part["drain"]} DRAIN BOSS</text>')
    b.append(f'<text x="{ox+6}" y="{floor+wt+86}" fill="{C_ACC}" font-size="17">FALL 2–3 ACROSS THE FLOOR TOWARD THE DRAIN BOSS →</text>')
    b.append(dim_h(ox,ox+L*s,oy+hp+124,'%d'%L,uid))
    b.append(dim_v(oy,oy+hp,ox-30,'%d'%Hh,uid))
    out['FRONT']=''.join(b)

    # ---------- PLAN: both penetrations dimensioned as tooling features ----------
    r=REG['TOP']; s=fit(L,Wd,r,76); ox,oy=centre(L*s,Wd*s,r)
    wt=max(T*s,3)
    t2=[frame(r), label(r,'PLAN VIEW','boss positions are tooling dimensions')]
    t2.append(f'<rect x="{ox}" y="{oy}" width="{L*s}" height="{Wd*s}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.4"/>')
    t2.append(f'<rect x="{ox+wt}" y="{oy+wt}" width="{L*s-2*wt}" height="{Wd*s-2*wt}" fill="var(--vp)" stroke="{C_OUT}" stroke-width="1.6"/>')
    t2.append(f'<text x="{ox+8}" y="{oy-12}" fill="{C_DIM}" font-size="17">REAR EDGE</text>')
    t2.append(f'<text x="{ox+8}" y="{oy+Wd*s+20}" fill="{C_DIM}" font-size="17">FRONT EDGE — AISLE SIDE</text>')
    by=oy+(Wd-bossy)*s
    for i in range(4):
        seg=(L*s-2*wt-16)/4
        xx=ox+wt+8+i*seg
        t2.append(f'<rect x="{xx+3}" y="{oy+(Wd*s-279*s)/2}" width="{seg-6}" height="{279*s}" fill="none" stroke="{C_ACC}" stroke-width="1.2" stroke-dasharray="10 6"/>')
    dx=ox+(L-part['drain_x'])*s
    t2.append(f'<line x1="{ox+wt}" y1="{by}" x2="{ox+L*s-wt}" y2="{by}" stroke="{C_CTR}" stroke-width="1" stroke-dasharray="22 6 4 6"/>')
    t2.append(f'<circle cx="{dx}" cy="{by}" r="{max(part["drain"]*s/2,7)}" fill="var(--hole)" stroke="{C_OUT}" stroke-width="2"/>')
    t2.append(f'<line x1="{dx}" y1="{by}" x2="{dx+30}" y2="{by-52}" stroke="{C_DIM}" stroke-width="1.2"/>')
    t2.append(f'<text x="{dx+34}" y="{by-56}" fill="{C_DIM}" font-size="18">⌀{part["drain"]} DRAIN</text>')
    if ovfx:
        vx=ox+(L-ovfx)*s
        t2.append(f'<circle cx="{vx}" cy="{by}" r="{max(ovfd*s/2,6)}" fill="none" stroke="{C_OUT}" stroke-width="2"/>')
        t2.append(f'<circle cx="{vx}" cy="{by}" r="{max(ovfd*s/2,6)+5}" fill="none" stroke="{C_OUT}" stroke-width="1.4"/>')
        t2.append(f'<line x1="{vx}" y1="{by}" x2="{vx-30}" y2="{by-52}" stroke="{C_DIM}" stroke-width="1.2"/>')
        t2.append(f'<text x="{vx-34}" y="{by-56}" fill="{C_DIM}" font-size="18" text-anchor="end">⌀{ovfd} OVERFLOW</text>')
        t2.append(dim_h(vx,ox+L*s,oy+Wd*s+46,'%d'%ovfx,uid))
    t2.append(dim_h(dx,ox+L*s,oy+Wd*s+74,'%d'%part['drain_x'],uid))
    t2.append(dim_v(by,oy+Wd*s,ox+L*s+34,'%d'%bossy,uid))
    t2.append(f'<text x="{ox+L*s/2}" y="{oy-64}" fill="{C_ACC}" font-size="17" text-anchor="middle">4 × 1020 TRAY POSITIONS SHOWN DASHED (REF ONLY)</text>')
    t2.append(dim_h(ox,ox+L*s,oy-36,'%d'%L,uid))
    t2.append(dim_v(oy,oy+Wd*s,ox-30,'%d'%Wd,uid))
    out['TOP']=''.join(t2)

    # ---------- END ----------
    r=REG['END']; s=fit(Wd,Hh*3,r,86); ox,oy=centre(Wd*s,max(Hh*s,40),r)
    hp2=max(Hh*s,40); wt2=max(T*s,3)
    e=[frame(r), label(r,'END VIEW','')]
    e.append(f'<rect x="{ox}" y="{oy}" width="{Wd*s}" height="{hp2}" fill="{C_FILL}" stroke="{C_OUT}" stroke-width="2.4"/>')
    e.append(f'<rect x="{ox+wt2}" y="{oy}" width="{Wd*s-2*wt2}" height="{hp2-wt2}" fill="var(--vp)" stroke="{C_OUT}" stroke-width="1.6"/>')
    bx=ox+(Wd-bossy)*s
    e.append(f'<line x1="{bx}" y1="{oy-16}" x2="{bx}" y2="{oy+hp2+16}" stroke="{C_CTR}" stroke-width="1" stroke-dasharray="22 6 4 6"/>')
    e.append(f'<text x="{bx}" y="{oy-22}" fill="{C_CTR}" font-size="16" text-anchor="middle">BOSS CL</text>')
    e.append(dim_h(ox,ox+Wd*s,oy+hp2+56,'%d'%Wd,uid))
    e.append(dim_v(oy,oy+hp2,ox-30,'%d'%Hh,uid))
    e.append(f'<text x="{ox+Wd*s+24}" y="{oy+hp2/2+7}" fill="{C_DIM}" font-size="19">t {T}</text>')
    out['END']=''.join(e)
    out['ISO']=iso_box(REG['ISO'],L,Wd,Hh,uid,label_txt='ISOMETRIC')
    return out

def iso_box(region,L,Wd,Hh,uid,broken=False,label_txt='ISOMETRIC'):
    x,y,rw,rh=region
    c30=math.cos(math.radians(30)); s30=math.sin(math.radians(30))
    Ld = L*0.34 if broken else L
    def P(px,py,pz): return ((px-py)*c30, (px+py)*s30-pz)
    pts=[P(0,0,0),P(Ld,0,0),P(Ld,Wd,0),P(0,Wd,0),P(0,0,Hh),P(Ld,0,Hh),P(Ld,Wd,Hh),P(0,Wd,Hh)]
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    sw=max(xs)-min(xs); sh=max(ys)-min(ys)
    s=min((rw-140)/max(sw,1),(rh-140)/max(sh,1))
    ox=x+(rw-sw*s)/2-min(xs)*s; oy=y+(rh-sh*s)/2-min(ys)*s
    def Q(i): return (ox+pts[i][0]*s, oy+pts[i][1]*s)
    def poly(idx,fill,op=1.0):
        d=' '.join('%.1f,%.1f'%Q(i) for i in idx)
        return f'<polygon points="{d}" fill="{fill}" fill-opacity="{op}" stroke="{C_OUT}" stroke-width="1.8" stroke-linejoin="round"/>'
    g=[frame(region), label(region,label_txt,'not to scale' if broken else '')]
    g.append(poly([4,5,6,7],'var(--iso-top)'))
    g.append(poly([0,1,5,4],'var(--iso-front)'))
    g.append(poly([1,2,6,5],'var(--iso-side)'))
    if broken:
        mx=(Q(1)[0]+Q(5)[0])/2
        g.append(f'<text x="{x+rw/2}" y="{y+rh-26}" fill="var(--ink3)" font-size="17" text-anchor="middle">length shortened for clarity</text>')
    return ''.join(g)

def sheet(part,uid):
    k=part['kind']
    if k=='tube': v=tube_long(part,uid)
    elif k=='tray': v=tray_views(part,uid)
    else: v=plate_views(part,uid)
    defs=(f'<defs><marker id="a1{uid}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">'
          f'<path d="M0,1.5 L10,5 L0,8.5 Z" fill="{C_DIM}"/></marker>'
          f'<marker id="a2{uid}" markerWidth="10" markerHeight="10" refX="1" refY="5" orient="auto">'
          f'<path d="M10,1.5 L0,5 L10,8.5 Z" fill="{C_DIM}"/></marker></defs>')
    # title block
    tbx,tby,tbw,tbh = 100, 1082, 1450, 62
    tb=[f'<rect x="{tbx}" y="{tby}" width="{tbw}" height="{tbh}" fill="var(--tb)" stroke="var(--line)" stroke-width="1.6"/>']
    cols=[('PART No.',part['pn'],250),('DESCRIPTION',part['name'],360),('MATERIAL',part['mat_short'],400),
          ('QTY/RACK',str(part['qty']),130),('MASS',part['mass'],130),('PROJECTION','',180)]
    cx=tbx
    for i,(k2,v2,w2) in enumerate(cols):
        if i: tb.append(f'<line x1="{cx}" y1="{tby}" x2="{cx}" y2="{tby+tbh}" stroke="var(--line)" stroke-width="1.2"/>')
        tb.append(f'<text x="{cx+12}" y="{tby+22}" fill="var(--ink3)" font-size="13" letter-spacing="1.2">{esc(k2)}</text>')
        tb.append(f'<text x="{cx+12}" y="{tby+48}" fill="var(--ink)" font-size="19" font-weight="600">{esc(v2)}</text>')
        cx+=w2
    # first-angle symbol
    sx=tbx+tbw-88
    tb.append(f'<g transform="translate({sx},{tby+40})"><ellipse cx="-16" cy="0" rx="7" ry="13" fill="none" stroke="var(--line)" stroke-width="1.6"/>'
              f'<path d="M6 -13 L26 -8 L26 8 L6 13 Z" fill="none" stroke="var(--line)" stroke-width="1.6"/>'
              f'<line x1="-30" y1="0" x2="34" y2="0" stroke="var(--ctr)" stroke-width="1" stroke-dasharray="8 3 2 3"/></g>')
    body=''.join(v[k3] for k3 in ('FRONT','END','TOP','ISO'))
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Four-view engineering drawing of {esc(part["name"])}">'
            f'{defs}<rect x="0" y="0" width="{W}" height="{H}" fill="var(--sheet)"/>'
            f'<g font-family="IBM Plex Mono, ui-monospace, monospace">{body}{"".join(tb)}</g></svg>')
