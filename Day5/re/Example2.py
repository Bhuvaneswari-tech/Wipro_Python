#Exact All numbers from a text

import re
txt = "The order IDs are 12345, 67890 and 22334"

numbers = re.findall(r'\d+',txt)
print('Extracted Numbers: ',numbers)