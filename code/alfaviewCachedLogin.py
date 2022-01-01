#!/usr/bin/env python3

import hfuLogin
import alfaviewEngine
import json, os, time

def isCacheFile(path='./cache.json'):
	return os.path.isfile(path)

def getCacheFile(path='./cache.json'):
	if isCacheFile(path):
		cacheFile= open(path, 'r')
		cacheContent= cacheFile.read()
		cacheFile.close()
		cacheValues = json.loads(cacheContent)

		return cacheValues
	else:
		return []

def setCacheFile(cacheValues, path='./cache.json'):
	configContent = json.dumps(configValues)

	configFile= open(path, 'w')
	configFile.write(configContent)
	configFile.close()

def cleanCache(cacheValues):
    newCacheValues=[]
    cutTime= time.time()-(12*60*60)
    
    for item in cacheValues:
        if item['timestamp'] >= cutTime:
            newCacheValues.append(item)
            
    return newCacheValues

def retrieveCache(cacheValues, key):
    for item in cacheValues:
        if item['key'] == key:
            return item

def start(myRoom, myUsername, myPassword, myName, alfaviewPath='/opt/alfaview/alfaview', timeout=15, bandWidthUsage='normal', noUpdate=0, skipQuickSetup=1, configDir='./'):
    cacheValues= getCacheFile(configDir + 'cache.json')
    cacheValues= cleanCache(cacheValues)
    cachedItem= retrieveCache(cacheValues, myRoom + myUsername + myName)
    if cachedItem == None:
        url= hfuLogin.getUrl(myRoom, myUsername, myPassword, myName, geckoLogPath=configDir+'geckodriver.log', webdriverPath=configDir, timeout=timeout)
        cachedItem= {'timestamp': time.time(), 'key': myRoom + myUsername + myName, 'url': url}
        cacheValues.append(cachedItem)
        setCacheFile(cacheValues, configDir + 'cache.json')
        
    alfaviewEngine.start(cachedItem['url'], bandWidthUsage=bandWidthUsage, noUpdate=noUpdate, skipQuickSetup=skipQuickSetup, alfaviewPath=alfaviewPath)
