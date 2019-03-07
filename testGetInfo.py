import requests

from bs4 import BeautifulSoup as sabaw
from selenium import webdriver
# driver = webdriver.Chrome(
#     executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Chrome\chromedriver")
# # driver = webdriver.Firefox(executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Firefox\geckodriver")

url = 'http://citwebdev033:1010/api/mcvehicle/vehicles?t=59511'
# driver.get(url)


page = requests.get(url).text
print(page)
