from _winreg import *
################################ 	9.	Windows Firewall With Advanced Security		#########################################
############################################	Domain Profile ##############################################################
#   9.1.1	Ensure 'Windows Firewall: Domain: Firewall state' is set to 'On (recommended)

def Firewallstate():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'EnableFirewall')[0])
	except:
		return "NOT FOUND"
	if value == 1 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.2	Ensure 'Windows Firewall: Domain: Inbound connections' is set to 'Block (default)'
def Inboundconnections():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'DefaultInboundAction')[0])
	except:
		return "NOT FOUND"
	if value == 1 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.3	Ensure 'Windows Firewall: Domain: Outbound connections' is set to 'Allow (default)'	
def Outboundconnections():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'DefaultOutboundAction')[0])
	except:
		return "NOT FOUND"
	if value == 0 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.4	Ensure 'Windows Firewall: Domain: Settings: Display a notification' is set to 'No'
def Displayanotification():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'DisableNotifications')[0])
	except:
		return "NOT FOUND"
	if value == 1 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.5	Ensure 'Windows Firewall: Domain: Settings: Apply local firewall rules' is set to 'Yes (default)'
def Applylocalfirewallrules():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'AllowLocalPolicyMerge')[0])
	except:
		return "NOT FOUND"
	if value == 1 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.6	Ensure 'Windows Firewall: Domain: Settings: Apply local connection security rules' is set to 'Yes (default)'
def Applylocalconnectionsecurityrules():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile', 0, KEY_READ)
		value = (QueryValueEx(key,'AllowLocalIPsecPolicyMerge')[0])
	except:
		return "NOT FOUND"
	if value == 1 :
		return 'OK'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.7	Ensure 'Windows Firewall: Domain: Logging: Name' is set to '%SYSTEMROOT%\System32\logfiles\firewall\domainfw.log'
def LoggingCustomizeName():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging', 0, KEY_READ)
		value = (QueryValueEx(key,'LogFilePath'))[0]
	except:
		return "OK"
	temp = "%systemroot%\system32\logfiles\\firewall\domainfw.log"
	if (value == temp )== 1:
		return 'GOOD'
	return 'WARNING'
	CloseKey(key)
	
#	9.1.8	Ensure 'Windows Firewall: Domain: Logging: Size limit (KB)' is set to '16,384 KB or greater'	
def LoggingCustomizeSize():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging', 0, KEY_READ)
		value = (QueryValueEx(key,'LogFileSize')[0])
	except:
		return "OK"
	if value >= 16384 :
		return 'GOOD'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.9	Ensure 'Windows Firewall: Domain: Logging: Log dropped packets' is set to 'Yes'
def Logdroppedpackets():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging', 0, KEY_READ)
		value = (QueryValueEx(key,'LogDroppedPackets')[0])
	except:
		return "OK"
	if value == 1 :
		return 'GOOD'
	return 'WARNING';
	CloseKey(key)
	
#	9.1.10	Ensure 'Windows Firewall: Domain: Logging: Log successful connections' is set to 'Yes'
def LogSuccessfulConnections():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging', 0, KEY_READ)
		value = (QueryValueEx(key,'LogSuccessfulConnections')[0])
	except:
		return "OK"
	if value == 1 :
		return 'GOOD'
	return 'WARNING';
	CloseKey(key)








