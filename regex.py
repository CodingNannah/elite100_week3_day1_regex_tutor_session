import re

with open('./files/regex-test.txt') as file:
    regex_data = file.readlines()
    

for line in regex_data: 
    names = re.compile(r'([A-Z][a-z]+)(\s[A-Z][a-z]*)?(\s[A-Z][a-z]+)')
    name = names.findall(line)
    if name: 
        print(name)
    else:
        print("None")
        
# for line in regex_data: 
#     f_name = re.compile(r'[A-Z][a-z]+')
#     m_name = re.compile(r'(\s[A-Z][a-z]*)?') # middle name = could be there but doesn't have to be! = ?
#     l_name = re.compile(r'\s[A-Z][a-z]+') 
#     names = f'{f_name} {m_name} {l_name}'
#     name = names.findall(line)
#     if name: 
#         print(name)
#     else:
#         print("None")
        
#     f_name = re.compile(r'[A-Z][a-z]+')
#     m_name = re.compile(r'(\s[A-Z][a-z]*)?') # middle name = could be there but doesn't have to be! = ?
#     l_name = re.compile(r'\s[A-Z][a-z]+') 


    # pattern.findall('string')
