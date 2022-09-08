import os
from datetime import date, datetime, time
import random
import variablestorage as locator
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException
import time
import AutomationTestTools as sf
#test supplemental data addition and verification relating to that

driver = sf.testlogin("https://stage.cozeva.com/patient_detail/1Y7FD8W?tab_type=CareOps&cozeva_id=1Y7FD8W&patient_id=9266593&cozeva_id=1Y7FD8W&session=YXBwX2lkPXJlZ2lzdHJpZXMmY3VzdElkPTE1MDAmZG9jdG9yc1BlcnNvbklkPTk2MjkxMTImZG9jdG9yX3VpZD05NjA5MDIzJnBheWVySWQ9MTUwMCZxdWFydGVyPTIwMjItMTItMzEmaG9tZT1ZWEJ3WDJsa1BYSmxaMmx6ZEhKcFpYTW1ZM1Z6ZEVsa1BURTFNREFtY0dGNVpYSkpaRDB4TlRBd0ptOXlaMGxrUFRFMU1EQSZmaWx0ZXJfb3JnX2lkPQ==&first_load=1")
sf.ajax_preloader_wait(driver)
found_suppdata = 0
non_com_measures = driver.find_element_by_id("table_1").find_elements_by_class_name("compliant_true")
while found_suppdata == 0:
    selected_measure = non_com_measures[sf.RandomNumberGenerator(len(non_com_measures), 1)[0]]
    if len(selected_measure.find_elements_by_class_name("pre_process_hcc")) == 0:
        continue
    else:
        found_suppdata = 1

selected_measure.find_element_by_class_name("addSuppData-trigger").click()
time.sleep(2)
selected_measure.find_element_by_class_name("pre_process_hcc").click()
time.sleep(2)

sf.ajax_preloader_wait(driver)
ele = driver.find_element_by_class_name("file_upload_attachment")
#ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'file_upload_attachment')))
dir = os.getcwd()
dir = os.path.join(dir, 'Assets\Doc_pdf.pdf')
print(dir)
ele.send_keys(dir)

time.sleep(2)

supdata = driver.find_element_by_class_name("saved_data")
supdata.find_element_by_class_name("datepicker").send_keys()


