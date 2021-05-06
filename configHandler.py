import json, os
from cryptography.fernet import Fernet

key= b'FpOza5rnPiW1Jv1oJzF6Ef0LitGrZ2nyQcPCG5kYmFc='
fernet = Fernet(key)

def isConfig(path='config.json'):
	if os.path.isfile(path):
		return True
	else:
		return False

def getConfig(path='config.json'):
	
	if os.path.isfile(path):
		configFile= open(path, 'r')
		configContent= configFile.read()
		configFile.close()
		configValues = json.loads(configContent)
		configValues['myPassword'] = fernet.decrypt(configValues['myPassword'].encode()).decode()
		return configValues
	else:
		return None

def setConfig(configValues, path='config.json'):
    configFile= open(path, 'w')
    configValues['myPassword'] = fernet.encrypt(configValues['myPassword'].encode()).decode()
    configContent = json.dumps(configValues)
    configFile.write(configContent)
    configFile.close()
