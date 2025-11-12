#john-123@example.com
#JOHN.DOE@example.COM
#charlie@gmail.com
#john@ex-ample.org
#john@123.com
#alice@example.in
#JOHN@EXAMPLE.COM

import re

email = "John.Doe@example.com"
#email="john.doe@example.com"
pattern = r'^[a-z0-9\.-]+@[a-z0-9\.-]+\.[a-z]{2,}$'

if re.match(pattern,email,re.IGNORECASE):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
    