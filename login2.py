from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
d = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
d.get('https://www.google.nl/')
print('HI I AM NIKHIL')