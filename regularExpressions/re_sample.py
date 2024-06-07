import re
phone = r"123-456-7890 # this is a phone number"
num = re.sub('\D','', phone)
print(num)
