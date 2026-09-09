from playwright.sync_api import sync_playwright
import pathlib
url='file://'+str(pathlib.Path('cea_rack_part_drawings.html').resolve())
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1280,'height':1000})
    pg.goto(url); pg.wait_for_timeout(2500)
    pg.screenshot(path='s_cover.png')
    el=pg.query_selector('#chRKA101')
    el.scroll_into_view_if_needed(); pg.wait_for_timeout(600)
    el.screenshot(path='s_upright.png')
    el2=pg.query_selector('#chRKA401')
    el2.scroll_into_view_if_needed(); pg.wait_for_timeout(600)
    el2.screenshot(path='s_tray.png')
    b.close()
print('ok')
