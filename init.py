from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userlogin import userLogin, userLoginIdirect
from search import searchFunc
from results import vehicleDetailInfo, retrieveSearchResultsOnePage, expandVehicleInfoIdirect, fetchIBCNum, fetchIBCandYOR, retrieveInfo, retrieveInfoUpd
from utils import printList, destructure, printDict, errorChecking, errorCheckUpd
from time import time
from traversePage import nextResults
from dataScraping import getAllInfo
import asyncio

# url = "http://auctions.autoterminal.co.nz/"
url = "http://www.ibcjapan.co.jp/"

username = "glabadia"
passcode = "Optiplex3050!"

# driver = webdriver.Chrome(executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Chrome\chromedriver")
driver = webdriver.Firefox(
    executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Firefox\geckodriver")
driver.get(url)

###
# Main Process
###

# userLogin(username, passcode, driver)
userLoginIdirect(username, passcode, driver)

# a = auctionHouseSearch()
# auctionHouseClick(a)
# conditionGrade()

searchFunc(driver)

getAllInfo(driver)
# expandVehicleInfoIdirect(driver)
# start = time()
# infoList = retrieveInfoUpd(driver)
# end = time()

# printDict(infoList)
# print(f"Finished in {end-start} seconds.")

# start = time()
# checkErrorList = errorCheckUpd(infoList)
# end = time()
# print(checkErrorList)
# print(f"There are {len(checkErrorList)} errors found.")
# print(f"Finished in {end-start} seconds.")
