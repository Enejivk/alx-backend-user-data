import re
email = 'enejivic@gmail.com'

value = re.search(r'.*@.*\.com', email)
if value:
    print(True)
else:
    print(False)