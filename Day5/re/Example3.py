#Valid phone number 

import re
#phone = "1234567890"
phone = "+91-6234567890"

#6,7,8,9
#\d+ = one or more digit
#\s+ - one or more spaces
pattern = r'^\+91-[6-9]\d{9}$'
#pattern = r'^+91[6-9]\d+$'

if re.match(pattern, phone):
    print('Valid Indian Phone number')
else:
    print('Invalid phone number')