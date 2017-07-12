from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType


desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities)
driver.get('https://ru.dotabuff.com/heroes/abaddon')
print(driver.page_source)