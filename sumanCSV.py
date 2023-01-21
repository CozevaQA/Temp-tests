def hccvalidation(driver, workbook, logger, screenshot_path, run_from):
    workbook.create_sheet('HCC Validation')
    ws = workbook['HCC Validation']

    ws.append(
        ['LOB', 'HCC Measure', 'Patient Non Compliant count(UI)', 'Patient Total count(UI)', 'HCC Score(UI)', 'Gaps',
         'Conditions',
         'Disconfirms', 'Clinical RAF', 'Potential RAF', 'Non Compliant Count(Export)', 'Total Count(Export)',
         'HCC Score Calculated(Export)',
         'Status', 'Comments'])
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    header.border = Border(bottom=Side(border_style="thin"))
    header.alignment = Alignment(horizontal="center", vertical="center")
    header_row = ws[1]
    for cell in header_row:
        cell.style = header
    red_background = PatternFill(patternType='solid', fgColor="00FF0000")
    green_background = PatternFill(patternType='solid', fgColor="50C878")
    gray_background = PatternFill(patternType='solid', fgColor="5F9EA0")
    # diff_style1 = DifferentialStyle(fill=red_background)
    # rule1 = Rule(type="text", dxf=diff_style1, text="Fail")
    # diff_style2 = DifferentialStyle(fill=green_background)
    # rule2 = Rule(type="text", dxf=diff_style2, text="Pass")
    # diff_style3 = DifferentialStyle(fill=gray_background)
    # rule3 = Rule(type="text", dxf=diff_style3, text="Unexecuted")

    ws.name = "Arial"
    test_case_id = 1

    def addition(total, row, switch, arr):
        try:
            for i in range(len(arr[1])):
                if switch == 1:
                    if str(arr[1][i]).endswith("Gaps"):
                        total = total + int(arr[row][i])
                if switch == 2:
                    if str(arr[1][i]).endswith("Conditions"):
                        total = total + int(arr[row][i])
                if switch == 3:
                    if str(arr[1][i]).endswith("Disconfirms"):
                        total = total + int(arr[row][i])
                if switch == 4:
                    if str(arr[1][i]).endswith("Clinical RAF"):
                        total = total + float(arr[row][i])
                if switch == 5:
                    if str(arr[1][i]).endswith("Potential RAF"):
                        total = total + float(arr[row][i])
                if switch == 6:
                    if str(arr[1][i]).endswith("Coded RAF"):
                        total = total + float(arr[row][i])

            return total
        except ValueError:
            print("No number detected in " + arr[1][i] + " .For row no = " + str(row + 1))
            return total

    def csvAddition(filepath):
        import csv
        with open(filepath, newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            rows = list(rows)
        Gaps = 0
        Conditions = 0
        Disconfirms = 0
        Clinical = 0
        Potential = 0
        Coded = 0
        for ind in range(2, len(rows)):
            Gaps = addition(Gaps, ind, 1, rows)
            Conditions = addition(Conditions, ind, 2, rows)
            Disconfirms = addition(Disconfirms, ind, 3, rows)
            Clinical = addition(Clinical, ind, 4, rows)
            Potential = addition(Potential, ind, 5, rows)
            Coded = addition(Coded, ind, 6, rows)
        print(Gaps)
        print(Conditions)
        print(Disconfirms)
        print(Clinical)
        print(Potential)
        print(Coded)
        print(len(rows) - 2)
        return Gaps, Conditions, Disconfirms, Clinical, Potential, Coded, (len(rows) - 2)


    sf.ajax_preloader_wait(driver)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='qt-filter-label']")))
    print("Selected page= " + driver.title)
    Registry_URL = driver.current_url
    sf.ajax_preloader_wait(driver)
    driver.find_element(By.XPATH, "//*[@id='qt-filter-label']").click()
    LOB_list = driver.find_element(By.XPATH, "//*[@id='filter-lob']").find_elements(By.TAG_NAME, 'li')
    for i in range(0, len(LOB_list)):
        LOB_Name = LOB_list[i].text
        print(LOB_Name)
        try:
            LOB_list[i].click()
        except ElementNotInteractableException as e:
            continue
        #LOB_list[i].click()
        driver.find_element(By.ID, "reg-filter-apply").click()
        LOB_Specific_URL = driver.current_url
        sf.ajax_preloader_wait(driver)
        if driver.find_element(By.XPATH, "//*[@id='conti_enroll']").is_selected():
            driver.find_element(By.XPATH, "//*[@class='cont_disc_toggle']").click()
        print(LOB_Specific_URL)
        HCC_measure_checklist = [33, 551, 552, 553, 554, 555, 556]
        for i in HCC_measure_checklist:
            flag = 0
            try:
                Measure_link = driver.find_element(By.XPATH, "//*[@id=" + str(i) + "]//a").get_attribute('href')
                Measure = driver.find_element(By.XPATH, "//*[@id=" + str(i) + "]//*[@class='met-name']").text
                print(Measure)
                print(Measure_link)
                driver.get(Measure_link)
                sf.ajax_preloader_wait(driver)
                #driver.implicitly_wait(3)
                ListRow = driver.find_element(By.XPATH, "//*[@id='metric-support-prov-ls']").find_element(By.TAG_NAME,
                                                                                                          "tbody").find_elements(
                    By.TAG_NAME, 'tr')
                if "No data available" in ListRow[0].text and len(ListRow) == 1:
                    Comments = "No provider data in HCC measure " + str(i)
                    print(Comments)
                    ws.append([LOB_Name, Measure, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'Undetermined',
                               Comments])
                elif len(ListRow) == 1:
                    ListRow[0].find_elements(By.TAG_NAME, 'a')[1].click()
                    sf.ajax_preloader_wait(driver)
                    print(driver.current_url)
                else:

                    Row = ListRow[random.randint(0, len(ListRow)-1)]
                    Row.find_elements(By.TAG_NAME, 'a')[1].click()
                    sf.ajax_preloader_wait(driver)
                    DataToBeValidated = driver.find_element(By.XPATH, "//*[@class='tab']").find_elements(By.TAG_NAME,
                                                                                                         'span')
                    print(driver.current_url)
                    DataToBeValidated_num = DataToBeValidated[0].text
                    DataToBeValidated_num = DataToBeValidated_num.replace(',', '')
                    print(DataToBeValidated_num)
                    DataToBeValidated_denum = DataToBeValidated[1].text
                    DataToBeValidated_denum = DataToBeValidated_denum.replace(',', '')
                    print(DataToBeValidated_denum)
                    driver.find_element(By.XPATH,
                                        "//*[@data-target='datatable_bulk_filter_0_quality_registry_list']").click()
                    driver.find_element(By.XPATH, "//*[contains(text(),'Export all to CSV')]").click()
                    sf.ajax_preloader_wait(driver)
                    onlyfiles = [f for f in listdir(locator.download_dir) if
                                 isfile(join(locator.download_dir, f))]
                    path = locator.download_dir + onlyfiles[0]
                    result = csvAddition(path)
                    os.remove(path)
                    if i == 553 or i == 556:
                        DataToBeValidated_num = float(DataToBeValidated_denum) - float(DataToBeValidated_num)
                        DataToBeValidated_num = round(DataToBeValidated_num, 3)
                        DataToBeValidated_denum = round(DataToBeValidated_denum, 3)
                        num = float(result[3] / result[6])
                        num = round(num, 3)
                        temp = float((result[5]-result[3])/result[6])
                        denum = float(result[4] / result[6])
                        denum = denum - temp
                        denum = round(denum, 3)
                        if abs(float(DataToBeValidated_num) - num) < 0.015 and abs(float(DataToBeValidated_denum) - denum) < 0.015:
                            ws.append([LOB_Name, Measure, "NA", "NA",
                                       str(DataToBeValidated_num) + "/" + str(DataToBeValidated_denum), "NA", "NA",
                                       "NA", result[3], result[4], "NA", "NA", str(num) + "/" + str(denum), 'Passed',
                                       "The HCC score for this measure is matching with UI and Export"])
                        else:
                            ws.append([LOB_Name, Measure, "NA", "NA",
                                       str(DataToBeValidated_num) + "/" + str(DataToBeValidated_denum), "NA", "NA",
                                       "NA", result[3], result[4], "NA", "NA", str(num) + "/" + str(denum), 'Failed',
                                       "The HCC score for this measure is not matching with UI and Export"])
                    else:
                        if int(DataToBeValidated_num) == int(result[0]) and int(DataToBeValidated_denum) == int(
                                result[0] + result[1] + result[2]):
                            ws.append(
                                [LOB_Name, Measure, DataToBeValidated_num, DataToBeValidated_denum, "NA", result[0],
                                 result[1],
                                 result[2], "NA", "NA", result[0], result[0] + result[1] + result[2], "NA", 'Passed',
                                 "The Compliant and total patient count of UI is matching with export"])

                            # ws.conditional_formatting.add("J1:O100", rule2)
                        else:
                            ws.append(
                                [LOB_Name, Measure, DataToBeValidated_num, DataToBeValidated_denum, "NA", result[0],
                                 result[1],
                                 result[2], "NA", "NA", result[0], result[0] + result[1] + result[2], "NA", 'Failed',
                                 'The Compliant and total patient count of UI is not matching with export'])
                            # ws.conditional_formatting.add("J1:O100", rule1)
            except NoSuchElementException:
                Comments = "HCC measure with id " + str(i) + " not found in LOB " + LOB_Name
                # ws.append([LOB_Name, str(i), '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'Unexecuted', Comments])
                # cellname = "N" + str(SheetRowName)
                # ws[''+cellname+''].fill = gray_background
                # # ws.conditional_formatting.add("J1:O100", rule3)
                print(Comments)
                if flag == 5:
                    print("No more HCC measures switching to next LOB")
            except Exception as e:
                traceback.print_exc()
                print(e)
            finally:
                flag += 1
                driver.get(LOB_Specific_URL)
                sf.ajax_preloader_wait(driver)
                #time.sleep(3)
                workbook.save(screenshot_path + "\\Report.xlsx")
        sf.ajax_preloader_wait(driver)
        driver.find_element(By.XPATH, "//*[@id='qt-filter-label']").click()
        LOB_list = driver.find_element(By.XPATH, "//*[@id='filter-lob']").find_elements(By.TAG_NAME, 'li')

    rows = ws.max_row
    cols = ws.max_column
    for i in range(2, rows + 1):
        for j in range(3, cols + 1):
            if ws.cell(i, j).value == 'Passed':
                ws.cell(i, j).fill = PatternFill('solid', fgColor='0FC404')
            elif ws.cell(i, j).value == 'Failed':
                ws.cell(i, j).fill = PatternFill('solid', fgColor='FC0E03')
            elif ws.cell(i, j).value == 'Undetermined':
                ws.cell(i, j).fill = PatternFill('solid', fgColor='808080')
            elif ws.cell(i, j).value == 'Data table is empty':
                ws.cell(i, j).fill = PatternFill('solid', fgColor='FCC0BB')