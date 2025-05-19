from firebasee.main1 import firebaseAPP
from pprint import pprint

result = firebaseAPP.delete('/students', "-OL_MCu6Aw_cXRrg8KyQ")

print(f"{result} record deleted")
