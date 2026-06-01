from selenium.webdriver.common.by import By

FLD_Firtsname       = (By.XPATH, "//input[@id='first-name']")
FLD_Lastname        = (By.XPATH, "//input[@id='last-name']")
FLD_ZIP_PostalCode  = (By.XPATH, "//input[@id='postal-code']")

BTN_Continue        = (By.XPATH, "//input[@id='continue']")
BTN_Finish          = (By.XPATH, "//button[@id='finish']")

TXT_CheckOut_Complte    = (By.XPATH, "//div[@class='header_secondary_container']")
TXT_ErrorMessageCO      = (By.XPATH, "//div[@class='error-message-container error']")