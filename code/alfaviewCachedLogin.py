import hfuLogin
import alfaviewEngine
import json, os

def isCache(path='./cache.json'):
	return os.path.isfile(path)

def getCache(path='./cache.json'):
	if isCache(path):
		cacheFile= open(path, 'r')
		cacheContent= cacheFile.read()
		cacheFile.close()
		cacheValues = json.loads(cacheContent)

def setCache(cacheValues, path='./cache.json'):
	configContent = json.dumps(configValues)

	configFile= open(path, 'w')
	configFile.write(configContent)
	configFile.close()

def start(myRoom, myUsername, myPassword, myName, timeout=15, alfaviewPath, bandWidthUsage='normal', noUpdate=0, skipQuickSetup=1, configDir='.'):
    hfuLogin.getUrl(myRoom, myUsername, myPassword, myName, geckoLogPath=configDir+'/geckodriver.log', webdriverPath=configDir, timeout=15)
    alfaviewEngine.start(url, bandWidthUsage='normal', noUpdate=noUpdate, skipQuickSetup=skipQuickSetup, alfaviewPath=alfaviewPath)



