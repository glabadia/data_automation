from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time
from utils import errorCheckUpd, printErrors, dictErrors, getAuctionHouse, printToFile, createDirectory, convert_time
from results import expandVehicleInfoIdirect, retrieveInfoTest, retrieveInfoUpd

from errorCheck import hasNoResults

import asyncio
WAIT_TIME: int = 10
SLEEP_TIME: int = 5


def nextResults(webdriver):
    '''
    #1  Get current page number
    #2  Get Next page number reference
    '''
    getActiveLink = "//ul[@class='pagination margin-top-bottom-none']//li[@class='active']"
    getNextLink = "/following-sibling::li[1]//a"

    infoList = []

    startDC = time()
    isEnd = False

    auctionHouseName = ""

    while not isEnd:
        print("Incur python to sleep..")

        sleep(SLEEP_TIME)

        expandVehicleInfoIdirect(webdriver)

        results = hasNoResults(webdriver)
        if results:
            print("No results displayed..")
            isEnd = True
            break

        if not auctionHouseName:
            auctionHouseName = getAuctionHouse(webdriver)

        start = time()
        infoList.extend(retrieveInfoUpd(webdriver))
        end = time()

        activePage = WebDriverWait(webdriver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, getActiveLink)))
        nextPage = WebDriverWait(webdriver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, f"{getActiveLink}/{getNextLink}")))

        print(f"Checking [Page {activePage.text}]..")

        if nextPage.text == "»":
            isEnd = True
            print("Traverse reached last page..")
            print()
        else:
            print(
                f"Finished checking [{auctionHouseName}, Page {activePage.text}] in {(end-start):.1f} seconds.")
            print()
            print(f"Next is [Page {nextPage.text}]..")
            nextPage.click()
    else:
        print("Traverse has reached the end.")
        print()

    endDC = time()

    timeDC = endDC-startDC
    print(f"Finished collecting data in {convert_time(timeDC)} seconds.")

    print(f"Will now check for errors..")
    print()
    startEC = time()
    checkErrorList = errorCheckUpd(infoList)

    populate_errors = dictErrors(checkErrorList[1])
    # print(populate_errors)
    print("----------------------------------------------------------")
    printErrors(populate_errors)
    endEC = time()
    timeEC = endEC - startEC
    printToFile((timeDC, timeEC), createDirectory(),
                auctionHouseName, populate_errors)

    print(f"Error checking done in {convert_time(timeEC)} seconds.")

    # check if //div[@id='loader'][contains(@style,'display: block;')] wait until display: none
    #   loader style --> display: block; top: 0px; bottom: 0px; left: 0px; right: 0px; position: fixed; background-color: rgba(255, 255, 255, 0.7); overflow: hidden; outline: none 0px; z-index: 999; text-align: center; margin-left: -15px; margin-right: -15px;
