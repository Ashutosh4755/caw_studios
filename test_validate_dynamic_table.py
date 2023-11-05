import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import pytest
from Common import common

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

#XPATH
table_data_button_xpath = "//summary[text()='Table Data']"
json_data_input_box = "//textarea[@id='jsondata']"
refresh_table_button = "//button[@id='refreshtable']"

def test_validate_table_data():
    #opened test data file
    common_obj = common()
    expected_dynamic_table_value = open('test_data.json',"r")
    expected_dynamic_table_value = expected_dynamic_table_value.read()
    #2- Click on Table Data button , a new input text box will be displayed:
    driver.find_element(By.XPATH,table_data_button_xpath).click()
    #cleared the input box
    driver.find_element(By.XPATH,json_data_input_box).clear()
    #3 - Insert the following data in input text box :
    # [{"name": "Bob", "age": 20, "gender": "male"}, {"name": "George", "age": 42, "gender": "male"}, {"name":"Sara","age": 42,"gender": "female"},
    #  {"name": "Conor", "age": 40, "gender": "male"}, {"name": "Jennifer", "age": 42, "gender": "female"}]
    driver.find_element(By.XPATH,json_data_input_box).send_keys(expected_dynamic_table_value)
    #And click on Refresh Table button.
    # 4.The entered data will be populated in the table.
    driver.find_element(By.XPATH,refresh_table_button).click()
    time.sleep(5)
    # 5. Now assert the data you have stored with the data that is populated in the UI table. Both data should match.
    cols = driver.find_elements(By.XPATH,"//table[@id='dynamictable']/tr/th")
    len_of_cols = len(cols)
    len_of_rows = len(driver.find_elements(By.XPATH,"//table[@id='dynamictable']/tr")) - 1
    lst = []
    #storing column names in a list
    for i in cols:
        lst.append(i.text)
    d = {}
    l1 = []
    #adding data one by one in a dictionary and then appending it in a list
    for i in range(2,len_of_rows+2):
        for j in range(1,len_of_cols+1):
            #converted string data to integer if we have age value.
            #We can add mobile number/pin code etc in future if we will have data for the same.
            #Otherwise we can convert every value of test_data file to string data type.
            if lst[j-1]=="age":
                d[lst[j - 1]] = int(driver.find_element(By.XPATH,"//table[@id='dynamictable']/tr[" + str(i) + "]/td" + "[" + str(j) + "]").text)
            else:
                d[lst[j - 1]] = driver.find_element(By.XPATH,"//table[@id='dynamictable']/tr[" + str(i) + "]/td" + "[" + str(j) + "]").text
        l1.append(d)
        d = {}
    actual_dynamic_table_value = str(l1).replace("'",'"')
    #called method to validate dynamic table
    common_obj.validate_dynamic_table(expected_dynamic_table_value,actual_dynamic_table_value)
    driver.close()


