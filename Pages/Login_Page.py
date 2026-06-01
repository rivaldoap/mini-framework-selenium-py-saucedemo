from selenium.webdriver.common.by import By

FLD_USERNAME      = (By.XPATH, "//input[@id='user-name']")
FLD_PASSWORD      = (By.XPATH, "//input[@id='password']")
BTN_LOGIN         = (By.XPATH, "//input[@id='login-button']")

TXT_LoginSuccess  = (By.XPATH, "//div[@class='header_secondary_container']")