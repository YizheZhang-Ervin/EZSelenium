from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# start browser
browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# open page
browser.get('https://www.baidu.com')
# output info
print(browser.title, browser.current_url)
# close page
browser.close()
# last page
browser.back()

# find elements by id
ele = browser.find_element_by_id('xxx')
# exact search
ele2 = browser.find_element_by_link_text('xxx')
# vague search
ele3 = browser.find_element_by_partial_link_text('xxx')
# xpath search
ele4 = browser.find_element_by_xpath('//*')
# clear element contents
ele.clear()
# simulate keyboard input
ele.send_keys('xxx')
# get element attributes
ele.get_attribute('xxx')
print(ele.size, ele.id)

# wait
browser.implicitly_wait(5)
WebDriverWait(browser, 5).until(lambda x: x.find_element_by_id('xxx'))

# quit browser
# browser.quit()
