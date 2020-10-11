'''
Created on Oct 11, 2020

@author: lenovo 

automation script for login to gmail account script. in progress..!!!

'''

from selenium import webdriver;


options=webdriver.ChromeOptions();
options.add_argument('--disable-infobars');
options.add_experimental_option("excludeSwitches", ['enable-automation']);
#driver = webdriver.Chrome(executable_path="E:/python_drivers/chromedriver_win32/chromedriver.exe",chrome_options=options) ;

driver=webdriver.Firefox(executable_path="E:/python_drivers/geckodriver-v0.27.0-win64/geckodriver.exe");

driver.get("https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AddSession")
driver.implicitly_wait(5)

driver.find_element_by_name("identifier").send_keys("immadipavankalyan55@gmail.com");




driver.find_element_by_class_name("VfPpkd-RLmnJb").click(); 

driver.implicitly_wait(5);

#//*[@id="identifierNext"]/div/button/div[2]
#//*[@id="identifierNext"]/div/button/div[2]