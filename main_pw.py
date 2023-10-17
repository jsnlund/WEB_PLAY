from playwright.sync_api import sync_playwright

if __name__ == "__main__":

    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge', headless=True)
        page = browser.new_page()
        page.goto('https://www.python.org')
        print(page.title())

        # search_bar = page.locator("[name='q']")
        search_bar = page.get_by_label("Main Navigation").get_by_role("link", name="News").click()
        # search_bar.clear()
        # search_bar.type("getting started with python")
        # search_bar.press('Enter')
        # page.wait_for_url("**/blogs")
        print(page.url)
        for link in page.get_by_role("link").all():
            # print(link)
            print(link.get_attribute('href'))

        # page.pause()



