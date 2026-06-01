import os
import time

from datetime import datetime
from selenium.common.exceptions import TimeoutException
from Pages.ObjectRepository_Global import *
from Pages.Login_Page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### HIGHLIGHT ###
def Highlight(driver, element, blink=5):

    for i in range(blink):
        # HIGHLIGHT ON
        driver.execute_script("""
            arguments[0].style.border='2px solid blue';
            arguments[0].style.boxShadow='0 0 5px blue';
        """, element)
        time.sleep(0.2)

        # HIGHLIGHT OFF
        driver.execute_script("""
            arguments[0].style.border='';
            arguments[0].style.boxShadow='';
        """, element)
        time.sleep(0.2)

# BASIC FUNCTION
def click(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    Highlight(driver, element)
    time.sleep(1.5)
    element.click()


def input_text(driver, locator, text, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    Highlight(driver, element)
    time.sleep(1.5)
    if text is None:
        text = ""
    element.clear()
    element.send_keys(text)


def get_text(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    Highlight(driver, element)
    time.sleep(1.5)
    return element.text


# Untuk menemukan produk yang ingin dipilih
def get_locator_produk(nama_produk):
    xpath_statis = (
        f"//div[text()='{nama_produk}']/ancestor::div[@class='inventory_item']"
    )
    # Kita cari tombol 'Add to cart' yang berada di dalam kotak produk tersebut
    return (By.XPATH, xpath_statis + "//button[text()='Add to cart']")

# SCROLL BERDASARKAN PIXEL (Misal: turun 500 pixel)
# Scroll layar berdasarkan koordinat X (horizontal) dan Y (vertical)
def scroll_by_pixel(driver, x=0, y=500):
    driver.execute_script(f"window.scrollBy({x}, {y});")
    time.sleep(1.5)


# Untuk scroll presisi ke object yang dituju
def scroll_to_element(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    # scroll element ke tengah layar
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", element
    )
    Highlight(driver, element)
    time.sleep(1.5)


# Scroll layar ke bagian paling atas halaman web
def scroll_to_top(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)


# Scroll layar keatas secara halus
def scroll_to_top_smooth(driver):
    driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
    time.sleep(1.5)


# Memastikan suatu element muncul di layar halaman web
def assert_element_displayed(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        Highlight(driver, element)
        # print(f"\n[ASSERT] Sukses! Element {locator} terlihat di layar.")
        assert element.is_displayed() is True
    except:
        assert False, f"Gagal! Element dengan locator {locator} tidak ditemukan atau tidak muncul di layar."


# Assertion untuk memastikan text yang muncul di web sesuai dengan ekspektasi sesuai data dari excel
def assert_text_equals_validasi(driver, locator, expected_text, timeout=10):
    try:
        # Tunggu sampai elemen tersebut benar-benar muncul di layar
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        Highlight(driver, element)
        # Mengambil text asli dari elemen web tersebut (.text)
        actual_text = element.text.strip()
        print(f"[ASSERT] Menyamakan teks. Web: '{actual_text}' | Excel: '{expected_text}'")
        
        # Melakukan pengujian / assertion
        assert actual_text == str(expected_text).strip(), \
            f"Gagal! Teks di web adalah '{actual_text}', tetapi ekspektasinya '{expected_text}'"
            
        print(f"[ASSERT] Sukses! Teks cocok sesuai ekspektasi.")
        
    except TimeoutException:
        raise AssertionError(f"Gagal! Elemen dengan locator {locator} tidak ditemukan dalam waktu {timeout} detik.")


# LOGOUT #
def logout(driver):
    click(driver, BTN_BurgerBar)
    click(driver, BTN_Logout)
    time.sleep(1.5)
    assert_element_displayed(driver, BOX_LoginWrapped)