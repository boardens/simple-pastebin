import mechanize

__version__ = "1.0.0"

br = mechanize.Browser()

def login(username, password):
	br.open("https://pastebin.com/login/")
	formcount = 0
	for frm in br.forms():  
		if str(frm.attrs["method"]) == "post":
			break
		formcount += 1
	br.select_form(nr=formcount)
	br["user_name"] = username
	br["user_password"] = password
	br.submit()
	if br.geturl() == "https://pastebin.com/u/"+username:
		return True
	for i in range(1, 7):
		if br.geturl() == "https://pastebin.com/login.php?e="+str(i):
			return False
	else:
		return False

def logout():
	try:
		br.open("https://pastebin.com/logout")
		return True
	except Exception:
		return False

def paste(content, name="", expire="N", exposure="0", formatting="1"):
	br.open("https://pastebin.com/")
	br.select_form("myform")
	br["paste_code"] = content
	br["paste_format"] = [formatting]
	br["paste_expire_date"] = [expire]
	br["paste_private"] = [exposure]
	br["paste_name"] = name
	br.submit()
	return br.geturl()
