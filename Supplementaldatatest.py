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
import AutomationTestTools as sf
#test supplemental data addition and verification relating to that

driver = sf.testlogin("https://stage.cozeva.com/patient_detail/1Y7FD8W?tab_type=CareOps&cozeva_id=1Y7FD8W&patient_id=9266593&cozeva_id=1Y7FD8W&session=YXBwX2lkPXJlZ2lzdHJpZXMmY3VzdElkPTE1MDAmZG9jdG9yc1BlcnNvbklkPTk2MjkxMTImZG9jdG9yX3VpZD05NjA5MDIzJnBheWVySWQ9MTUwMCZxdWFydGVyPTIwMjItMTItMzEmaG9tZT1ZWEJ3WDJsa1BYSmxaMmx6ZEhKcFpYTW1ZM1Z6ZEVsa1BURTFNREFtY0dGNVpYSkpaRDB4TlRBd0ptOXlaMGxrUFRFMU1EQSZmaWx0ZXJfb3JnX2lkPQ==&first_load=1")
sf.ajax_preloader_wait(driver)
