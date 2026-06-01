from openpyxl import load_workbook

FILE_PATH = r"Utils/Excel/Checkout/Checkout_Positive.xlsx"

def checkout():
    workbook = load_workbook(FILE_PATH)
    sheet = workbook["CHECKOUT"]

    all_data = []

    # min_row=2 : Otomatis skip baris 1 (Header)
    # max_col=5 : Membaca dari Kolom A (RUN) sampai Kolom E (ZIP_POSTALCODE)
    for row in sheet.iter_rows(min_row=2, max_col=10, values_only=True):

        # row[0] adalah Kolom A. Jika isinya "RUN", ambil data di baris tersebut
        if row[0] is None:
            continue

        if str(row[0]).strip().upper() == "RUN":
            all_data.append(
                {
                "TC": row[1],
                "NAMA_PRODUK_1": row[2],
                "NAMA_PRODUK_2": row[3],
                "FIRSTNAME": row[4],
                "LASTNAME": row[5],
                "ZIP_POSTALCODE": row[6],
                }
            )

    return all_data