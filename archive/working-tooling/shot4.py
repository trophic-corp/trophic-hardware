from playwright.sync_api import sync_playwright
import re,io
s=io.open('cea_rack_part_drawings.html',encoding='utf-8').read()
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1300,'height':1200})
    pg.set_content('<!doctype html><html><head><meta charset=utf8></head><body>'+s+'</body></html>',wait_until='networkidle')
    for sel,out in [('#chRKA401','t_tray.png'),('#chRKA104','t_brace.png')]:
        el=pg.query_selector(sel)
        el.scroll_into_view_if_needed()
        el.screenshot(path=out)
        print('shot',out)
    b.close()
