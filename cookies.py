from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")

time_start= time.time()
#set playing time to 5 minutes
time_run =  60*5


i=5
while time.time() < time_start+time_run:
    time_now = time.time()
    cookie.click()
    if time_now > time_start + i:
        i += 5
        right_pannels = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]
        money_required = [int(pannel.text.split("-")[1].strip().replace(",", "")) for pannel in right_pannels]

        add_ons = driver.find_elements(By.CSS_SELECTOR, "#store b ")[:-1]
        add_ons_list = [add_on.text.split("-")[0].strip() for add_on in add_ons]


        buy_list = [{money_required[n]: add_ons_list[n]} for n in range(0, len(money_required))]



        money = int(driver.find_element(By.ID, "money").text.replace(",",""))

        max_amount = 0
        for amount in money_required:
            if money > amount:
                max_amount = amount
        if max_amount > 0:
            index = money_required.index(max_amount)
            buy = driver.find_element(By.ID, f"buy{buy_list[index][max_amount]}")
            buy.click()





