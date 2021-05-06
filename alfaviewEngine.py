import os, sys

def start(url, bandWidthUsage='normal', noUpdate=0, skipQuickSetup=1, alfaviewPath=''):
	if alfaviewPath:
		if sys.platform.startswith('win'):
			cmd= 'start /D '+alfaviewPath+' alfaview.exe '
		if sys.platform.startswith('linux'):
			#TODO
			pass
	else:
		if sys.platform.startswith('win'):
			cmd= 'start /D "%AppData%\\..\\Local\\alfaview\\app" alfaview.exe '
		if sys.platform.startswith('linux'):
			#TODO
			pass
		
	if noUpdate:
		cmd= cmd + '--noupdate '
	
	if bandWidthUsage == 'normal':
		cmd= cmd + '--bandwidthUsage normal '
	elif bandWidthUsage == 'reduced':
		cmd= cmd + '--bandwidthUsage reduced '
	elif bandWidthUsage == 'minimum':
		cmd= cmd + '--bandwidthUsage minimum '
	
	if skipQuickSetup:
		cmd= cmd + '--skipquicksetup '
	
	cmd= cmd + '--url "' + url + '"'
	
	os.system(cmd)
