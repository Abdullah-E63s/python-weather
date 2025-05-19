from firebasee.main1 import firebaseAPP
from pprint import pprint

result = firebaseAPP.put('/students/-OL_MCu6Aw_cXRrg8KyQ', "height", 3.25)


pprint(result)