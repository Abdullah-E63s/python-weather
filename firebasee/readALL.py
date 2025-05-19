from firebasee.main1 import firebaseAPP
from pprint import pprint

result = firebaseAPP.get('/students', None)

pprint(result)