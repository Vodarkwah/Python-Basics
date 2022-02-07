# JSON tutorial

import json
                #JSON is more like a dictionary. ( Presents data as nested lists and dic)
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#  "name" : "Chuck"
#   key       value            ',' is used to separate a certain k-v term
# line 7-10 represents objects within object

info = json.loads(data)     # parses the str
print('Name:',info["name"]) # prints the val of key 'name' in info
print('Hide:',info["email"]["hide"])