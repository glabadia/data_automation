from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME: int = 10


def userLogin(un, pw, driver):
    """
    automates userLogin
    """
    # UserId, Password, btnlogin
    driver.find_element_by_id("UserId").send_keys(un)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_id("btnlogin").click()


def userLoginIdirect(un, pw, driver):
    """
    automates userLogin
    """
    # div.@id=navigation-wrapper
    # div.navbar-header
    # div.add_on_menu_for_ipad hidden-lg hidden-xs
    # div.login_ipad visible-md visible-sm login_form
    # a.btn btn-primary
    # //div[@class='nav navbar-nav navbar-right visible-lg login_form']//a[@class='btn btn-primary'][contains(text(),'Login')]
    loginPath = "//div[@id='login_container_web']//a[@class='btn btn-primary'][contains(text(),'Login')]"
    # loginButton = "//div[@id='navigation-wrapper']/div[@class='navbar-header']/div[@class='add_on_menu_for_ipad hidden-lg hidden-xs']/div[@class='login_ipad visible-md visible-sm login_form']/a[@class='btn btn-primary']"
    loginButton = WebDriverWait(driver, SLEEP_TIME).until(
        EC.presence_of_element_located((By.XPATH, loginPath)))
    loginButton.click()
    # driver.find_element_by_xpath(loginButton).click()

    driver.find_element_by_id("username").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("login-command").click()
