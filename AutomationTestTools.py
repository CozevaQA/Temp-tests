from datetime import date, datetime, time
import random
import variablestorage as locator
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import py_compile

def testlogin(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    #options.add_argument(locator.chrome_profile_path)  # Path to your chrome profile
    # options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox");
    options.add_argument("--dns-prefetch-disable");
    driver = webdriver.Chrome(executable_path='assets/chromedriver.exe', options=options)
    login_to_cozeva(driver)
    driver.get(URL)
    return driver

def login_to_cozeva(driver):
    driver.get(locator.logout_link)
    driver.get(locator.login_link)
    driver.maximize_window()
    file = open(r"assets\loginInfo.txt", "r+")
    details = file.readlines()
    driver.find_element_by_id("edit-name").send_keys(details[0].strip())
    driver.find_element_by_id("edit-pass").send_keys(details[1].strip())
    file.seek(0)
    file.close()
    driver.find_element_by_id("edit-submit").click()
    time.sleep(2)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "reason_textbox")))
    driver.find_element_by_id("reason_textbox").send_keys(details[4].strip())
    time.sleep(0.5)
    driver.find_element_by_id("edit-submit").click()
    ajax_preloader_wait(driver)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, locator.xpath_filter_measure_list)))
    print("Logged in to Cozeva!")

def date_time():
    today = date.today()
    tz_In = pytz.timezone('Asia/Kolkata')
    datetime_In = datetime.now(tz_In)
    time = datetime_In.strftime("[%I-%M-%S %p]")
    now = str(today) + time
    return now


def ajax_preloader_wait(driver):
    time.sleep(1)
    #WebDriverWait(driver, 300).until(
    #    EC.invisibility_of_element((By.XPATH, "//div/div[contains(@class,'ajax_preloader')]")))
    WebDriverWait(driver, 300).until(
        EC.invisibility_of_element((By.CLASS_NAME, "ajax_preloader")))
    #time.sleep(1)
    if len(driver.find_elements_by_class_name("ajax_preloader")) != 0:
        WebDriverWait(driver, 300).until(
            EC.invisibility_of_element((By.CLASS_NAME, "ajax_preloader")))
    time.sleep(1)




def CheckAccessDenied(string):
    sub_str = "/access_denied"
    if string.find(sub_str) == -1:
        # print("Access check done")
        return 0
    else:
        print("ACCESS DENIED has been found!!")
        return 1


def CheckErrorMessage(driver):
    err_msg = 0
    sub_str = "error"
    toast_messages = driver.find_elements_by_xpath("//div[@class='drupal_message_text']")
    if (len(toast_messages)) != 0:
        i = 1
        while i <= len(toast_messages):
            toast_message_xpath_new = "(//div[@class='drupal_message_text'])" + str([i])
            toast_message = driver.find_element_by_xpath(toast_message_xpath_new).text
            if toast_message.count(sub_str) > 0:
                err_msg = 1
                break
            i += 1
        if err_msg == 1:
            return 1
        else:
            return 0
    else:
        return 0


def RandomNumberGenerator(maximum_range,number):
    a = []
    a = random.sample(range(1, maximum_range), number)
    #print(a)
    return a

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_css(driver, css):
    try:
        driver.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(driver, id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True