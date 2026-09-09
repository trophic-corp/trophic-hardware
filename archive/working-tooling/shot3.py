from playwright.sync_api import sync_playwright
import pathlib
url='file://'+str(pathlib.Path('cea_room_phase2.html').resolve())
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1360,'height':1000})
    pg.goto(url); pg.wait_for_timeout(2200)
    el=pg.query_selector('.dwg'); el.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    el.screenshot(path='room.png')
    b.close()
print('ok')
