
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

if __name__ == "__main__":

    service= Service()
    options = webdriver.EdgeOptions()
    # options.add_experimental_option("detach", True) # to allow browser to remain open after execution
    options.add_argument("--headless=new")
    driver = webdriver.Edge(service=service, options=options)

    driver.get('https://www.python.org')
    print(driver.title)
    search_bar = driver.find_element(By.NAME, "q")

    search_bar.clear()
    search_bar.send_keys("getting started with python")
    search_bar.send_keys(Keys.RETURN)

    print(driver.current_url)
    # driver.close()