import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='msedge', headless=True)
        page = await browser.new_page()
        await page.goto('https://www.python.org')
        print(await page.title())

        # search_bar = page.locator("[name='q']")
        search_bar = await page.get_by_label("Main Navigation").get_by_role("link", name="News").click()
        # search_bar.clear()
        # search_bar.type("getting started with python")
        # search_bar.press('Enter')
        # page.wait_for_url("**/blogs")
        print(page.url)
        for link in await page.get_by_role("link").all():
            # print(link)
            print(link.get_attribute('href'))
        await browser.close()


if __name__ == "__main__":

    asyncio.run(main())



