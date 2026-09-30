import asyncio, glob, os, shutil
from playwright.async_api import async_playwright
B='/workspace/ind-wi-dashboard'; URL='file://'+B+'/dashboard.html'
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch()
        pg=await br.new_page(viewport={'width':1600,'height':900},device_scale_factor=1)
        await pg.goto(URL); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=B+'/dashboard.png',full_page=True)
        await pg.close()
        vd=B+'/_vid'; shutil.rmtree(vd,ignore_errors=True)
        ctx=await br.new_context(viewport={'width':1600,'height':900},record_video_dir=vd,record_video_size={'width':1600,'height':900})
        pg=await ctx.new_page(); await pg.goto(URL); await pg.wait_for_timeout(3000)
        for i in range(3):  # linger on Star Performers photo cards
            bb=await pg.locator('.star').nth(i).bounding_box()
            await pg.mouse.move(bb['x']+60,bb['y']+bb['height']/2,steps=20); await pg.wait_for_timeout(1200)
        async def hover(sel,fx,fy,ms=1800):
            bb=await pg.locator(sel).bounding_box()
            await pg.mouse.move(bb['x']+bb['width']*fx,bb['y']+bb['height']*fy,steps=25); await pg.wait_for_timeout(ms)
        await hover('#c_runs',0.45,0.2); await hover('#c_runs',0.6,0.72)
        await hover('#c_bowl',0.35,0.6); 
        async def scroll_to(y,dur=2500):
            cur=await pg.evaluate('window.scrollY'); n=50
            for i in range(1,n+1):
                await pg.evaluate(f'window.scrollTo(0,{cur+(y-cur)*i/n})'); await pg.wait_for_timeout(dur//n)
        y=await pg.evaluate("document.getElementById('c_worm').getBoundingClientRect().top+window.scrollY-120")
        await scroll_to(y); await pg.wait_for_timeout(800)
        await hover('#c_worm',0.55,0.35); await hover('#c_worm',0.8,0.2)
        await hover('#c_mix',0.3,0.5); await hover('#c_bnd',0.25,0.7)
        y=await pg.evaluate("document.getElementById('c_man').getBoundingClientRect().top+window.scrollY-120")
        await scroll_to(y); await hover('#c_man',0.6,0.4)
        y=await pg.evaluate("document.body.scrollHeight-900"); await scroll_to(y,4000); await pg.wait_for_timeout(2500)
        await pg.mouse.move(400,300,steps=10)
        await scroll_to(0,3000); await pg.wait_for_timeout(800)
        # slicer demo
        await pg.click('#slicer button[data-t="India"]'); await pg.wait_for_timeout(2500)
        await pg.click('#slicer button[data-t="West Indies"]'); await pg.wait_for_timeout(2500)
        await pg.click('#slicer button[data-t="All"]'); await pg.wait_for_timeout(2000)
        v=pg.video; await ctx.close(); src=await v.path(); await br.close()
        os.replace(src,B+'/_raw.webm')
asyncio.run(main())
