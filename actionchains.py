from selenium.webdriver.common.action_chains import ActionChains
from webdriver import ele, ele2

# Action Chains: input events
# generate simulate action
act = ActionChains(ele)
act2 = act.move_to_element(ele2)
# execute saved action
act2.perform()
