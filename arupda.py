# Capture
# screenshot:
# == == == == == == == == == == == == == == == == == == == == == =

def captureScreenshot(self, driver, page_title, screenshot_path):
    self.driver = driver

    try:
        self.screenshot_path = screenshot_path
        self.page_title = page_title
        date = datetime.now().strftime('%H_%M_%S_%p')

        # bad_chars = [';', ':', '|', ' ']
        # for i in bad_chars:
        #     final_title_text = page_title.replace(i, '_')
        #     self.driver.save_screenshot(self.screenshot_path + "/" + final_title_text + "_" + str(date) + ".png")
        self.driver.save_screenshot(self.screenshot_path + "/" + self.page_title + "_" + str(date) + ".png")

    except Exception as e:
        print(e)


# Checking
# default
# CE
# status in Registry
# page:
# == == == == == == == == == == == == == == == == == == == == == == == == == == =

CE_checkbox = self.driver.find_element_by_xpath("//*[@id='conti_enroll']")
# print(CE_checkbox)

if (CE_checkbox.is_selected()):
    CEstatus = 'Y'

else:
    CEstatus = 'N'

OA_Nav_obj4 = OARoleNavigation(self.driver)
OA_Nav_obj4.checkCEOnOff(CEstatus, targetpath, screenshot_path)  # calling CE validation function

# the following code reset the CE status in Registry page after checking CE on/off

self.driver.find_element_by_xpath("//*[@id='metric_scorecard']/div/div[1]/div/div/div/div[2]/label").click()
time.sleep(2)
LOBdropdownelement = self.driver.find_element_by_xpath("//*[@id='qt-filter-label']")
LOBdropdownelement.click()
self.driver.find_element_by_xpath("//*[@id='reg-filter-apply']").click()

# CE
# validation in each
# LoB:
# == == == == == == == == == == == == == == == == == == =

def CheckCEOnOff(self, CEstatus, targetpath, screenshot_path):
    self.CEstatus = CEstatus
    file = 'config.ini'
    config = ConfigParser()
    dirpath = os.path.dirname(__file__)
    config.read(dirpath + "\\" + file)
    time.sleep(2)
    loader = WebDriverWait(self.driver, 300)
    loader.until(EC.invisibility_of_element_located((By.XPATH, "//div/div[contains(@class,'ajax_preloader')]")))
    if (self.CEstatus == "Y"):
        try:
            print("CE Toggle is in ON state............")
            self.driver.find_element_by_xpath("//*[@id='metric_scorecard']/div/div[1]/div/div/div/div[2]/label").click()
            time.sleep(4)
            print("Now CE Toggle is in OFF state............")
            LOBdropdownelement = self.driver.find_element_by_xpath("//*[@id='qt-filter-label']")
            LOBdropdownelement.click()
            LOBquarter = LOBdropdownelement.find_elements_by_xpath("//*[@id='filter-quarter']/li")
            LOBname = LOBdropdownelement.find_element_by_xpath("//*[@id='filter-lob']")
            LOBnamelist = LOBname.find_elements_by_tag_name("li")
            Payername = LOBdropdownelement.find_elements_by_xpath("//*[@id='filter-payer']")
            for i in range(0, len(LOBnamelist)):
                LOBName = LOBnamelist[i].text
                print(LOBnamelist[i].text)
                print("--------------------------------")
                if (LOBnamelist[i].text == ""):
                    print("LOB is hidden")
                else:
                    LOBnamelist[i].click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//*[@id='reg-filter-apply']").click()
                    loader = WebDriverWait(self.driver, 300)
                    loader.until(
                        EC.invisibility_of_element_located((By.XPATH, "//div/div[contains(@class,'ajax_preloader')]")))
                    time.sleep(2)
                    self.Log_obj.captureScreenshot(self.driver, LOBName, screenshot_path)
                    supportRegistry = self.driver.find_element_by_xpath("//*[@id='registry_body']")
                    measureList = supportRegistry.find_elements_by_tag_name("li")
                    print(len(measureList))
                    if (len(measureList) == 0):
                        print("CE OFF : LOB is BLANK")
                        self.Log_obj.critical(
                            "CE OFF -> Registry is BLANK for : " + LOBName + " .Please check.",
                            targetpath)
                    else:
                        print("CE OFF : LOB is Okay")

                    LOBdropdownelement = self.driver.find_element_by_xpath("//*[@id='qt-filter-label']")
                    LOBdropdownelement.click()
                    LOBname = LOBdropdownelement.find_element_by_xpath("//*[@id='filter-lob']")
                    LOBnamelist = LOBname.find_elements_by_tag_name("li")


        except Exception as e:
            self.Log_obj.critical("CE ON -> Navigation suspended due to some unexpected error.Please check.",
                                  targetpath)


    else:
        try:
            print("CE Toggle is in OFF state............")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='metric_scorecard']/div/div[1]/div/div/div/div[2]/label").click()
            time.sleep(2)
            print("Now CE Toggle is in ON state............")
            LOBdropdownelement = self.driver.find_element_by_xpath("//*[@id='qt-filter-label']")
            LOBdropdownelement.click()
            LOBname = LOBdropdownelement.find_element_by_xpath("//*[@id='filter-lob']")
            LOBnamelist = LOBname.find_elements_by_tag_name("li")
            Payername = LOBdropdownelement.find_elements_by_xpath("//*[@id='filter-payer']")
            for i in range(0, len(LOBnamelist)):
                LOBName = LOBnamelist[i].text
                print(LOBnamelist[i].text)
                print("--------------------------------")
                if (LOBnamelist[i].text == ""):
                    print("LOB is hidden")
                else:
                    LOBnamelist[i].click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//*[@id='reg-filter-apply']").click()
                    loader = WebDriverWait(self.driver, 300)
                    loader.until(
                        EC.invisibility_of_element_located((By.XPATH, "//div/div[contains(@class,'ajax_preloader')]")))
                    time.sleep(2)
                    self.Log_obj.captureScreenshot(self.driver, LOBName, screenshot_path)
                    supportRegistry = self.driver.find_element_by_xpath("//*[@id='registry_body']")
                    measureList = supportRegistry.find_elements_by_tag_name("li")
                    print(len(measureList))
                    if (len(measureList) == 0):
                        print("CE ON : LOB is BLANK")
                        self.Log_obj.critical("CE ON -> Registry is BLANK for : " + LOBName + " Please check.",
                                              targetpath)
                    else:
                        print("CE ON : LOB is Okay")

                    LOBdropdownelement = self.driver.find_element_by_xpath("//*[@id='qt-filter-label']")
                    LOBdropdownelement.click()
                    LOBname = LOBdropdownelement.find_element_by_xpath("//*[@id='filter-lob']")
                    LOBnamelist = LOBname.find_elements_by_tag_name("li")


        except Exception as e:
            print("Exception in CE Off.")
            self.Log_obj.critical("CE OFF -> Navigation suspended due to some unexpected error.Please check.",
                                  targetpath)


# Time
# Capsule
# validation:
# == == == == == == == == == == == == == == == == == == == == == == == == == ==

# In between latest two computation cards, date should not be equal.

if (applink_text == "Time Capsule"):

    try:
        if (self.driver.find_element_by_xpath("//*[@id='computation']").is_displayed()):
            self.driver.find_element_by_xpath("//*[@id='computation']/div[2]/div[1]/div[1]").click()
            time.sleep(2)
            card_title = self.driver.find_element_by_xpath("//*[@class='card-title']/div[1]").text
            try:
                computation_date1 = self.driver.find_element_by_xpath(
                    "//*[@card_type='computation']/div[1]/div/div/div/div[1]").text
                computation_date2 = self.driver.find_element_by_xpath(
                    "//*[@card_type='computation']/div[2]/div/div/div/div[1]").text
                time.sleep(1)
                print(computation_date1)
                print(computation_date2)
                if (computation_date1 == computation_date2):
                    print("ERROR!! Both computation dates are same")
                    self.Log_obj.critical("Computation Dates are Invalid ", targetpath)
                else:
                    print("Both computation dates are Valid")
                    self.Log_obj.info("Computation Dates are Valid ", targetpath)
                self.Log_obj.captureScreenshot(self.driver, "Card_details", screenshot_path)

            except Exception as e1:
                print("Single computation date is available")
                self.Log_obj.captureScreenshot(self.driver, "Card_details", screenshot_path)

    except Exception as e:
        self.Log_obj.warning("Time Capsule -> Computation Section is not available.",
                             targetpath)
    try:
        if (self.driver.find_element_by_xpath(
                "//*[@id='computation']/following-sibling::div[1]").is_displayed()):
            self.Log_obj.info("Time Capsule -> Inbound Section is available.", targetpath)
    except Exception as e:
        self.Log_obj.warning("Time Capsule -> Inbound Section is not available.",
                             targetpath)

    try:
        if (self.driver.find_element_by_xpath(
                "//*[@id='computation']/following-sibling::div[2]").is_displayed()):
            self.Log_obj.info("Time Capsule -> Outbound Section is available.", targetpath)
    except Exception as e:
        self.Log_obj.warning("Time Capsule -> Outbound Section is not available.",
                             targetpath)
    try:
        no_data_text = self.driver.find_element_by_xpath(
            "//*[@class='content']/div/div/b").text
        if (no_data_text == "No Data Available."):
            self.Log_obj.critical("Time Capsule -> No data available.Please check.",
                                  targetpath)
    except Exception as e:
        print("Time Capsule is appearing properly.")

# Group - 1, Group - 2
# Verification:
# == == == == == == == == == == == == == == == == == == == == == == =

def groupvalidation(self, targetpath, screenshot_path):
    try:
        context_dropdown_arrow = self.driver.find_element_by_xpath("//*[@id='context_dropdown_arrow']")
        # print("Arrow found")
        context_dropdown_arrow.click()
        time.sleep(3)
        group_list_container = self.driver.find_element_by_xpath("//*[@id='ul_1']")
        group_list_element = group_list_container.find_elements_by_tag_name("li")
        randomList = random.choices(group_list_element, k=1)  # randomly 1 group is checking
        for i in range(0, len(randomList)):
            print(randomList[i].text)
            group_name = randomList[i].text
            randomList[i].click()
            time.sleep(5)
            # print("Arrow found....2")
            try:
                group2_list_container = self.driver.find_element_by_xpath("//*[@id='ul_2']")
                group2_list_element = group2_list_container.find_elements_by_tag_name("li")
                group2_list_element_count = len(group2_list_element)
                randomList2 = random.choices(group2_list_element, k=1)  # randomly 1 group is checking
                for i in range(0, len(randomList2)):
                    print(randomList2[i].text)
                    group_name2 = randomList2[i].text
                    group_all = (group_name + "_" + group_name2)
                    print(group_all)
                    try:
                        randomList2[i].click()
                        time.sleep(5)
                        access_check = self.URLAccessCheck(targetpath)
                        if (access_check):
                            self.Log_obj.captureScreenshot(self.driver, group_name2, screenshot_path)
                            self.Log_obj.critical(
                                "Group List ->  Access Denied found on clicking " + group_all + " .Please check.",
                                targetpath)
                        else:
                            # self.Log_obj.captureScreenshot(self.driver, group_name2, screenshot_path)

                            self.GroupNavigation(targetpath, screenshot_path, group_all)
                    except Exception as e:
                        print(e)
                        self.Log_obj.critical(
                            "Group Navigation -> Issue occurred while navigating to Group1-Group2 : " + group_all,
                            targetpath)

                    context_dropdown_arrow = self.driver.find_element_by_xpath("//*[@id='context_dropdown_arrow']")
                    context_dropdown_arrow.click()
                    group2_list_container = self.driver.find_element_by_xpath("//*[@id='ul_2']")
                    # print("Arrow found....3")
                    group2_list_element = group2_list_container.find_elements_by_tag_name("li")
                    randomList2 = random.choices(group2_list_element, k=1)

            except Exception as e:
                try:
                    access_check = self.URLAccessCheck(targetpath)
                    if (access_check):
                        self.Log_obj.captureScreenshot(self.driver, group_name, screenshot_path)
                        self.Log_obj.critical(
                            "Group List ->  Access Denied found on clicking " + group_name + " .Please check.",
                            targetpath)
                    else:
                        # self.Log_obj.captureScreenshot(self.driver, group_name, screenshot_path)
                        print("Test.......1")
                        self.GroupNavigation(targetpath, screenshot_path, group_name)
                except Exception as e:
                    self.Log_obj.critical(
                        "Group Navigation -> Issue occurred while navigating to Group1 : " + group_name, targetpath)
            context_dropdown_arrow = self.driver.find_element_by_xpath("//*[@id='context_dropdown_arrow']")
            context_dropdown_arrow.click()
            time.sleep(5)
            group_list_container = self.driver.find_element_by_xpath("//*[@id='ul_1']")
            group_list_element = group_list_container.find_elements_by_tag_name("li")
            randomList = random.choices(group_list_element, k=1)

        self.driver.refresh()
        time.sleep(3)

    except Exception as e:
        print("Group1 is not available or having some issue while navigating.")
        self.Log_obj.info("** Group1 is not available or having some issue while navigating.", targetpath)

