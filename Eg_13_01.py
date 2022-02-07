#Examoke from Ch 13

import xml.etree.ElementTree as ET  # Built in XML Parser

data = ''' 
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)      # converts the str data into a tree form or reads the data

print('Name:', tree.find('name').text) # Find text in the name tag
print('Attr:', tree.find('email').get('hide')) # Find coontent of the hide attribute