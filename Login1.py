from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox") #This make Chromium reachable
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-default-browser-check") #Overrides default choices
options.add_argument("--no-first-run")
options.add_argument("--disable-default-apps")

driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
driver.get('https://www.google.co.in/')