from firebasee.main1 import firebaseAPP
from pprint import pprint
# creates functions 

data = {
    "name" : "alex",
    "age" : 56,
    "Height" : 6.00,
    "school" : "lions school"
}

result = firebaseAPP.post('/students', data)


pprint(result)