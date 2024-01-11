import re

fail_tee = r'C:\Users\37259\Desktop\Kolm.txt'

with open(fail_tee, encoding="UTF-8") as fail:
   tekst = fail.read()

muster = r'(\+372)* *(\d{3,4}) *(\d{4})'
vastus = re.findall(muster, tekst)
formatted_numbers = []

for match in vastus:
   country_code = match[0] if match[0] else ''
   number = f"{country_code}{match[1]}{match[2]}"
   formatted_numbers.append(number)

print(formatted_numbers)