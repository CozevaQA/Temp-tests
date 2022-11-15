import selenium
import AutomationTestTools as sf

driver = sf.testlogin("http://stage.cozeva.com")
sf.ajax_preloader_wait(driver)

