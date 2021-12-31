import json, os
from cryptography.fernet import Fernet

key= b'FpOza5rnPiW1Jv1oJzF6Ef0LitGrZ2nyQcPCG5kYmFc='
fernet = Fernet(key)

def isConfig(path='config.json'):
	return os.path.isfile(path)

def getConfig(path='config.json'):
	if isConfig(path):
		configFile= open(path, 'r')
		configContent= configFile.read()
		configFile.close()
		configValues = json.loads(configContent)

		if not 'myRoom' in configValues:
			configValues['myRoom'] = None
		if not 'myUsername' in configValues:
			configValues['myUsername'] = None
		if not 'myPassword' in configValues:
			configValues['myPassword'] = None
		if not 'myName' in configValues:
			configValues['myName'] = None
		# TODO: rest dazu

		configValues['myPassword'] = fernet.decrypt(configValues['myPassword'].encode()).decode()

		return configValues
	else:
		return { 'myRoom': None, 'myUsername': None, 'myPassword': None, 'myName': None } # TODO: rest dazu

def setConfig(configValues, path='config.json'):
    configFile= open(path, 'w')
    configValues['myPassword'] = fernet.encrypt(configValues['myPassword'].encode()).decode()
    configContent = json.dumps(configValues)
    configFile.write(configContent)
    configFile.close()
