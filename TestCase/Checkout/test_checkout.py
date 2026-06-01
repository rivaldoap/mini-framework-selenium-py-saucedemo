import os
import sys
import time

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)

import pytest
from Pages.ObjectRepository_Global import *
from Pages.CheckOut_Page import *
# Import file-nya saja, JANGAN import fungsi test_login secara langsung
from TestCase.Login import test_login
from Utils.helper import *
from Utils.Excel.Checkout.ExcelReader_Checkout_Positive import (
    checkout as read_excel_positive
    )
from Utils.Excel.Checkout.ExcelReader_Checkout_Negative import (
    checkout as read_excel_negative
    )

daftar_baris_run_positive = read_excel_positive()

@pytest.mark.parametrize("data_excel", daftar_baris_run_positive)
def test_checkout_positive(data_excel):
    if not data_excel:
        pytest.skip("Tidak ada baris data yang ditandai 'RUN'.")

    driver = test_login.test_login()

    try:
        list_produk_kolom = [
            data_excel.get("NAMA_PRODUK_1"),
            data_excel.get("NAMA_PRODUK_2"),  
            # Tambahkan NAMA_PRODUK_3 dst jika ada nanti
        ]

        for nama_produk in list_produk_kolom:
            # JIKA KOLOM DI EXCEL KOSONG ATAU BERISI NONE, LEWATI (JANGAN DI-KLIK)
            if nama_produk is None or str(nama_produk).strip() == "":
                continue

            nama_produk_target = str(nama_produk).strip()
            print(f"\n[PROSES] Mencari & klik produk: {nama_produk_target}")

            BTN_AddToCart = get_locator_produk(nama_produk_target)

            scroll_to_element(driver, BTN_AddToCart)
            click(driver, BTN_AddToCart)
            time.sleep(1)

            # Setelah loop produk selesai kemudian menuju keranjang
        scroll_to_top_smooth(driver)
        click(driver, LNK_ShoppingCart)
        time.sleep(2)

        scroll_to_element(driver, BTN_CheckOut)
        click(driver, BTN_CheckOut)

        scroll_to_top_smooth(driver)
        input_text(driver, FLD_Firtsname, data_excel["FIRSTNAME"])
        input_text(driver, FLD_Lastname, data_excel["LASTNAME"])
        input_text(driver, FLD_ZIP_PostalCode, data_excel["ZIP_POSTALCODE"])

        scroll_to_element(driver,BTN_Continue)
        click(driver, BTN_Continue)
        scroll_to_element(driver, BTN_Finish)
        click(driver, BTN_Finish)

        scroll_to_element(driver, TXT_CheckOut_Complte)
        assert_element_displayed(driver, TXT_CheckOut_Complte)

    finally:
        if driver is not None:
            logout(driver)
            driver.quit()

#................. NEGATIVE .................#
daftar_baris_run_negative = read_excel_negative()
@pytest.mark.parametrize("data_excel", daftar_baris_run_negative)
def test_checkout_negative(data_excel):
    if not data_excel:
        pytest.skip("Tidak ada data.")
    
    # Jika tipe data di Excel BUKAN NEGATIVE, lewati fungsi ini
    tipe_test = str(data_excel.get("TYPE", "POSITIVE")).strip().upper()
    if tipe_test != "NEGATIVE":
        pytest.skip(f"Data ini bertipe {tipe_test}, dilewati oleh Negative Test.")

    id_test_case = data_excel.get("TC", "TC_UNKNOWN")
    print(f"\n[RUNNING NEGATIVE] -> {id_test_case}")

    driver = test_login.test_login()

    try:
        list_produk_kolom = [
            data_excel.get("NAMA_PRODUK_1"),
            data_excel.get("NAMA_PRODUK_2"),  
            # Tambahkan NAMA_PRODUK_3 dst jika ada nanti
        ]

        pilih_produk = False
        for nama_produk in list_produk_kolom:
            # JIKA KOLOM DI EXCEL KOSONG ATAU BERISI NONE, LEWATI (JANGAN DI-KLIK)
            if nama_produk is None or str(nama_produk).strip() == "":
                continue

            pilih_produk = True

            nama_produk_target = str(nama_produk).strip()
            print(f"\n[PROSES] Mencari & klik produk: {nama_produk_target}")

            BTN_AddToCart = get_locator_produk(nama_produk_target)

            scroll_to_element(driver, BTN_AddToCart)
            click(driver, BTN_AddToCart)
            time.sleep(1)

            # Setelah loop produk selesai, baru menuju keranjang
        scroll_to_top_smooth(driver)
        click(driver, LNK_ShoppingCart)
        time.sleep(2)

        scroll_to_element(driver, BTN_CheckOut)
        click(driver, BTN_CheckOut)

        scroll_to_top_smooth(driver)
        input_text(driver, FLD_Firtsname, data_excel["FIRSTNAME"])
        input_text(driver, FLD_Lastname, data_excel["LASTNAME"])
        input_text(driver, FLD_ZIP_PostalCode, data_excel["ZIP_POSTALCODE"])

        scroll_to_element(driver,BTN_Continue)
        click(driver, BTN_Continue)

        cek_form_excel = (
            (data_excel.get("FIRSTNAME") is None or str(data_excel.get("FIRSTNAME")).strip() == "") and
            (data_excel.get("LASTNAME") is None or str(data_excel.get("LASTNAME")).strip() == "") and
            (data_excel.get("ZIP_POSTALCODE") is None or str(data_excel.get("ZIP_POSTALCODE")).strip() == "")
        )

        if not pilih_produk:
            if cek_form_excel:
                # Tidak Pilih Produk & Ada Form Kosong
                print(f"[INFO] TC {id_test_case}: Tidak memilih produk DAN Form Kosong. Validasi error message form.")
                pesan_error_target = data_excel.get("EXPECTED_TEXT")
                assert_text_equals_validasi(driver, TXT_ErrorMessageCO, pesan_error_target)
            
            else:
                # Tidak Pilih Produk TAPI Form Diisi
                print(f"[INFO] TC {id_test_case}: Tidak memilih produk TAPI Form Diisi. Melanjutkan ke Finish.")
                scroll_to_element(driver, BTN_Finish)
                click(driver, BTN_Finish)
                print(f" STATUS: PASSED -> [{id_test_case}] Berhasil checkout tanpa produk.")
        
        else:
            # Pilih Produk TAPI Ada Form Kosong
            pesan_error_target = data_excel.get("EXPECTED_TEXT")
            assert_text_equals_validasi(driver, TXT_ErrorMessageCO, pesan_error_target)

    except Exception as e:
        raise e
    
    finally:
        if driver is not None:
            logout(driver)
            driver.quit()