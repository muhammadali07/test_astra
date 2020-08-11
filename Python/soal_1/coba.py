
from datetime import datetime, date

print("Your date of birth (dd-mm-yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def calculate_month(born):
    today = date.today()
    return today.month - born.month - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)
month = calculate_month(date_of_birth)

print(age, "Tahun", month, "Bulan")
