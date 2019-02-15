from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置chrome无界面模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driverChrome = webdriver.Chrome(options=chrome_options)
driverChrome.get("https://www.baidu.com")

print(driverChrome.current_url)