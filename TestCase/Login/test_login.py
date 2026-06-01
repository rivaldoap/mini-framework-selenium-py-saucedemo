import time
from Utils.driver_factory import start_browser
from Utils.helper import *
from _DataLogin.excel_reader_login import get_login_data

from Pages.Login_Page import *

def test_login():
    # START BROWSER
    driver = start_browser()

    # GET DATA FROM EXCEL
    data = get_login_data()

    # OPEN URL
    driver.get(data["URL"])

    # LOGIN
    input_text(driver, FLD_USERNAME, data["USERNAME"])
    input_text(driver, FLD_PASSWORD, data["PASSWORD"])
    click(driver, BTN_LOGIN)
    assert_element_displayed(driver, TXT_LoginSuccess)

    print("Login Success")
    time.sleep(1.5)
    # driver.quit()
    return driver