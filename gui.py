import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
#own stuff
import configHandler, hfuLogin, alfaviewEngine

#shared Variables
threadHfuLoginStatus=2
alfaviewUrl=''

def threadHfuLogin(myRoom, myUsername, myPassword, myName, timeoutArg):
	global threadHfuLoginStatus
	global alfaviewUrl

	try:
		alfaviewUrl= hfuLogin.getUrl(myRoom, myUsername, myPassword, myName, timeout=timeoutArg)
		threadHfuLoginStatus=0
	except:
		threadHfuLoginStatus=1

def openConfig(parent):
		myRoom = tk.StringVar()
		myUsername = tk.StringVar()
		myPassword = tk.StringVar()
		myName = tk.StringVar()
		bandWidth = tk.StringVar()
		timeout = tk.StringVar()

		newWindow = tk.Toplevel(parent)
		newWindow.title("Configuration")
		newWindow.geometry("250x390")
		newWindow.resizable(False, False)
		newWindow.iconbitmap('icon.ico')
		tk.Label(newWindow, text ="Here you can set your HFU credentials\nand configure defaults").pack()
		# create options frame
		options = ttk.Frame(newWindow)
		options.pack(padx=10, pady=10, fill='x', expand=True)

		def setConfig(event=0):
			timeoutNew=15
			if timeout.get():
				timeoutNew= timeout.get()

			configValues= {'myRoom':myRoom.get(),
							'myUsername':myUsername.get(),
							'myPassword':myPassword.get(),
							'myName':myName.get(),
							'bandWidth':bandWidth.get(),
							'timeout':timeoutNew}
			print(configValues)
			configHandler.setConfig(configValues)
			newWindow.destroy()

		# room form
		roomForm = ttk.Label(options, text="Default Room:")
		roomForm.pack(fill='x', expand=True)

		roomForm = ttk.Entry(options, textvariable=myRoom)
		roomForm.pack(fill='x', expand=True)
		roomForm.focus()

		# username form
		userForm = ttk.Label(options, text="HFU Username:")
		userForm.pack(fill='x', expand=True)

		userForm = ttk.Entry(options, textvariable=myUsername)
		userForm.pack(fill='x', expand=True)

		# password form
		passForm = ttk.Label(options, text="HFU Password\n(Will be obfuscated and saved in config!):")
		passForm.pack(fill='x', expand=True)

		passForm = ttk.Entry(options, textvariable=myPassword, show='*')
		passForm.pack(fill='x', expand=True)

		# name form
		nameForm = ttk.Label(options, text="Name for Alfaview Session:")
		nameForm.pack(fill='x', expand=True)

		nameForm = ttk.Entry(options, textvariable=myName)
		nameForm.pack(fill='x', expand=True)

		# bandwidth form
		bandWidthForm = ttk.Label(options, text="Bandwith option\nnormal / reduced / minimum\n(Leave blank for default 'normal'):")
		bandWidthForm.pack(fill='x', expand=True)

		bandWidthForm = ttk.Entry(options, textvariable=bandWidth)
		bandWidthForm.pack(fill='x', expand=True)

		# timeout form
		timeoutForm = ttk.Label(options, text="Timout (Leave blank for default of 15)")
		timeoutForm.pack(fill='x', expand=True)

		timeoutForm = ttk.Entry(options, textvariable=timeout)
		timeoutForm.pack(fill='x', expand=True)

		if configHandler.isConfig():
			configData= configHandler.getConfig()

			roomForm.insert(0, configData['myRoom'])
			userForm.insert(0, configData['myUsername'])
			passForm.insert(0, configData['myPassword'])
			nameForm.insert(0, configData['myName'])
			bandWidthForm.insert(0, configData['bandWidth'])
			timeoutForm.insert(0, configData['timeout'])

		# set button
		set_button = ttk.Button(options, text="Apply Config", command=setConfig)
		set_button.pack(fill='x', expand=True, pady=10)

		# login with ENTER
		newWindow.bind('<Return>', setConfig)

def global_checkStatus(root):
	global threadHfuLoginStatus
	global alfaviewUrl
	configData= configHandler.getConfig()
	bandWidth= 'normal'
	if configData['bandWidth']:
		bandWidth= configData['bandWidth']

	if threadHfuLoginStatus==0:
		alfaviewEngine.start(alfaviewUrl, bandWidthUsage=bandWidth, noUpdate=0, skipQuickSetup=1, alfaviewPath='')
		root.destroy()
	if threadHfuLoginStatus==1:
		msg = (f'We are sorry to inform you that an error occurred.\n'
				'This could either be because you entered wrong information or due to a bug in the app.')
		messagebox.showerror(title='ERROR OCCURRED', message=msg)
		root.destroy()
	if threadHfuLoginStatus==2:
		#do nothing
		pass

def main():
	# root window
	root = tk.Tk()
	root.geometry("300x170")
	root.resizable(False, False)
	root.title('betawatch')
	root.iconbitmap('icon.ico')

	# store room nr
	room = tk.StringVar()

	def checkStatus():
		global_checkStatus(root)
		root.after(10, checkStatus)

	def login_clicked(event=0):
		label["text"] = 'Entering room, please wait...'
		configData= configHandler.getConfig()
		myRoom= configData['myRoom']
		timeout= 15;

		if room.get():
			myRoom= room.get()
		try:
			configData['timeout']= int(configData['timeout'])
			if 3 <= configData['timeout'] <= 40:
				timeout= configData['timeout']
		except:
			pass

		arguments= (myRoom,
					configData['myUsername'],
					configData['myPassword'],
					configData['myName'],
					timeout,)

		hfuLoginThread = threading.Thread(target=threadHfuLogin, args=(arguments), daemon=True)
		hfuLoginThread.start()
		checkStatus()


	# create signin frame
	signin = ttk.Frame(root)
	signin.pack(padx=10, pady=10, fill='x', expand=True)

	# options button
	options = ttk.Button(signin, text="Options", command=lambda: openConfig(root))
	options.pack(padx=100, pady=10, fill='x', expand=True)

	# room number form
	roomForm = ttk.Label(signin, text="Room (leave blank for default from config):")
	roomForm.pack(fill='x', expand=True)

	roomForm = ttk.Entry(signin, textvariable=room)
	roomForm.pack(fill='x', expand=True)
	roomForm.focus()

	# login button
	login_button = ttk.Button(signin, text="Login", command=login_clicked)
	login_button.pack(fill='x', expand=True, pady=10)

	# login with ENTER
	root.bind('<Return>', login_clicked)

	# Entering text
	label = tk.Label(signin, text="")
	label.pack(fill='x', expand=True)

	def checkConfig():
		if not configHandler.isConfig():
			openConfig(root)

	root.after(0, checkConfig)

	root.mainloop()


if __name__ == "__main__":
	main()
