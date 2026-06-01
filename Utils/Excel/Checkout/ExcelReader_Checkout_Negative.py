from openpyxl import load_workbook

FILE_PATH = r"Utils/Excel/Checkout/Checkout_Negative.xlsx"

def checkout():
    workbook = load_workbook(FILE_PATH)
    sheet = workbook["CHECKOUT"]

    all_data = []

    # min_row=2 : Otomatis skip baris 1 (Header)
    # max_col=5 : Membaca dari Kolom A (RUN) sampai max_col (max_col bisa diubah sesuai kebutuhan, max_col diberi batasan supaya tidak terlalu lama membaca kolom excel)
    for row in sheet.iter_rows(min_row=2, max_col=10, values_only=True):

        # row[0] adalah Kolom A. Jika isinya "RUN", ambil data di baris tersebut
        if row[0] is None:
            continue

        if str(row[0]).strip().upper() == "RUN":
            all_data.append(
                {
                "TC": row[1],
                "TYPE": row[2],
                "NAMA_PRODUK_1": row[3],
                "NAMA_PRODUK_2": row[4],
                "FIRSTNAME": row[5],
                "LASTNAME": row[6],
                "ZIP_POSTALCODE": row[7],
                "EXPECTED_TEXT": row[8]
                }
            )

    return all_data