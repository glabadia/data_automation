from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time
from userlogin import userLogin, userLoginIdirect
from search import searchFunc, auctionHouseClick, auctionHouseSearch
from results import vehicleDetailInfo, retrieveSearchResultsOnePage, expandVehicleInfoIdirect, fetchIBCNum, fetchIBCandYOR, retrieveInfo, retrieveInfoUpd
from utils import printList, destructure, printDict, errorCheckUpd
from traversePage import nextResults
from dataScraping import getAllInfo

url = "http://www.ibcjapan.co.jp/"
home_driver = r"E:\personal\program\chromedriver"
firefox_driver = r"E:\personal\program\geckodriver"

username = "glabadia"
passcode = "Optiplex3050!"

# driver = webdriver.Firefox(executable_path=firefox_driver)
# driver = webdriver.Chrome(executable_path=home_driver)
# driver = webdriver.Chrome(executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Chrome\chromedriver")
driver = webdriver.Firefox(
    executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Firefox\geckodriver")
driver.get(url)

###
# Main Process
###

# userLogin(username, passcode, driver)
userLoginIdirect(username, passcode, driver)

a = auctionHouseSearch(driver)
auctionHouseClick(driver, a)
# conditionGrade()

# searchFunc(driver)

# nextResults(driver)
