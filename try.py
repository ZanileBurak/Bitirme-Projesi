import xml.etree.ElementTree as ET
import random
tree = ET.parse('new_set.xml')
root = tree.getroot()
list = []

data = ET.Element('data')





userlist = []
for stri in root:
    if(stri[5].text not in userlist):
        userlist.append(stri[5].text)
    print(stri[5].text,"checked")
    
for i in range(len(userlist)):
    list.append(round(random.randint(50,150)/100,1))
i=0
for a in userlist:
    print(a)

for stri in userlist:
    row = ET.SubElement(data, 'row')
    ET.SubElement(row, 'USER_ID').text = stri
    ET.SubElement(row, 'PASSWORD').text = "12345"
    ET.SubElement(row, 'PRICE_FACTOR').text = str(list[i])

    i+=1


        

b_xml = ET.tostring(data)        
with open("users.xml", "wb") as f:
    f.write(b_xml)
