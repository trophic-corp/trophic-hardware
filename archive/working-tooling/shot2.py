from playwright.sync_api import sync_playwright
import pathlib
url='file://'+str(pathlib.Path('cea_rack_systems_spec.html').resolve())
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1360,'height':1000})
    pg.goto(url); pg.wait_for_timeout(2500)
    for i,el in enumerate(pg.query_selector_all('.dwg')):
        el.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
        el.screenshot(path=f'd{i}.png')
    b.close()
print('ok')
