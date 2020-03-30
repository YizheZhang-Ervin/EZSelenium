from webdriver import ele, browser

# fill in form and click
ele.send_keys('xxx')
ele.click()

# switch windows
browser.switch_to_window(browser.window_handles[1])

# alert
alert = browser.switch_to_alert()
# alert info
print(alert.text)
# accept/dismiss alert
alert.accept()
alert.dismiss()