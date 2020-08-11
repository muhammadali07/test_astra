from datetime import datetime, date

nama = input("Masukkan Nama :")
email = input ("Massukan Email :")
tgl_lhr = datetime.strptime(input ("Massukkan tanggal lahir (DD-MM-YYYY) :"), "%d %m %Y")

def cal_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def cal_month(born):
    today = date.today()
    return today.month - born.month - ((today.month, today.day) < (born.month, born.day))

age = cal_age(tgl_lhr)
month = cal_month(tgl_lhr)

print("=======================================")
print("Nama Anda :", nama)
print("Email Anda :", email)
print("Usia Anda :", age, "Tahun", month, "Bulan")
