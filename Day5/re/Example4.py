#Replace multiple spaces with a single space

#strip - removes starting and ending spaces

#txt = 'Hello         welcome      to       Python'

# import re
# txt = 'Hello         welcome      to       Python'
# cleaned_txt = re.sub(r'\s+',' ',txt)

# print("Before:",txt)
# print('After:',cleaned_txt)

import re
#Extract All words starting with Capital Letter
txt = "Python is created by Guido van Roosum in the Netherlands"
#Python Guido Roosum Netherlands

captial = re.findall(r'\b[A-Z][A-z]*\b',txt)

print('Word starting with capital letter:',captial)