import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = None
text = "Rasberry pi hosted website for iot project."

# get login creds from creds.json
def getCreds():
    print("getting creds")
    data = None
    with open("creds.json") as json_file:
        data = json.load(json_file)
        return data["email"], data["password"]


def start_browser_and_login():

    global driver

    print("starting browser...")

    # start browser
    driver = webdriver.Chrome(service_log_path="NUL")
    driver.get("https://pagekite.net/home/")

    # wait for page
    WebDriverWait(driver, 10000).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )

    login()


def login():
    global driver

    print("login...")

    # get creds for login
    email, password = getCreds()

    # login required
    emailField = driver.find_element_by_xpath(
        '//*[@id="loginTable"]/tbody/tr[2]/td[1]/input'
    )
    emailField.click()
    emailField.send_keys(email)
    passwordField = driver.find_element_by_xpath(
        '//*[@id="loginTable"]/tbody/tr[3]/td[1]/input'
    )
    passwordField.click()
    passwordField.send_keys(password + Keys.ENTER)

    print("logged")

    time.sleep(2)

def go_to_pricing():
    global driver

    print("go to ...")

    driver.get("https://pagekite.net/signup/?more=bw")

    # wait for page
    WebDriverWait(driver, 10000).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )

    price = driver.find_element_by_xpath('//*[@id="pwyw-amt"]')
    price.click()
    price.clear()


def get_it_for_free():
    global driver

    print("get free")

    message = driver.find_element_by_xpath(
        '//*[@id="div-pwyw"]/div[2]/div[4]/div/form/p[1]/textarea'
    )
    message.click()
    message.send_keys(text)

    check = driver.find_element_by_xpath('//*[@id="pwyw-broke-checkbox"]')
    check.click()

    send = driver.find_element_by_xpath(
        '//*[@id="div-pwyw"]/div[2]/div[4]/div/form/p[2]/input'
    )
    send.click()

    print("done")

    time.sleep(2)


def main():
    start_browser_and_login()
    go_to_pricing()
    get_it_for_free()
    driver.close()


if __name__ == "__main__":
    main()
