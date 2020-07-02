from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanize

__version__ = "1.0.0"

br = mechanize.Browser()
logged = False

expire_values = [
	"N", "10M", "1H",
	"1D", "1W", "2W",
	"1M", "6M", "1Y"
	]

exposure_values = [
	"public",
	"unlisted",
	"private"
	]

format_values = [None,
	"text", "actionscript", "ada", "apache", "applescript",
	"arm_nasm", "asp", "bash", "c", "c_mac",
	"caddcl", "cadlisp", "cpp", "csharp", "coldfusion",
	"css", "d", "delphi", "diff", "batch",
	"eiffel", "fortran", "freebasic", "gml", "html4strict",
	"ini", "java", "javascript", "lisp", "lua",
	None, "mpasm", "mysql", "nsis", "objc",
	"ocaml", "oobas", "oracle8", "pascal", "perl",
	"php", "python", "qbasic", "robots", "ruby",
	"scheme", "smarty", "sql", None, "vb",
	"vbnet", "visualprofox", "xml", "autolt", "blitzbasic",
	"bnf", "erlang", "genero", "groovy", "haskell",
	"inno", "latex", "lsl2", "matlab", "m68k",
	"mirc", "rails", "plsql", "smalltalk", "tcl",
	None, "z80", "abap", "actionscript3", "apt_sources",
	"avisynth", "basic4gl", "bibtex", "bf", "boo",
	"cfdg", "cil", "cmake", "cobol", "dcs",
	"div", "dot", "email", "fo", "gettext",
	"glsl", "gnuplot", "hq9plus", "idl", "intercal",
	"io", "java5", "kixtart", "klonec", "klonecpp",
	"locobasic", "lolcode", "lotusformula", "lotusscript", "lscript",
	"make", "modula3", "mxml", "oberon2", "ocaml_brief",
	"oracle11", "per", "php_brief", "pic16", "pixelblender",
	"povray", "powershell", "progress", "prolog", "properties",
	"providex", "rebol", "reg", "sas", "scala",
	"scilab", "sdlbasic", "terarerm", "thinbasic", "tsql",
	"typoscript", "verilog", "vhdl", "vim", "visualprolog",
	"whitespace", "whois", "winbatch", "xorg_conf", "xpp",
	"pawn", "4cs", "6502acme", "6502kickass", "6502tasm",
	"68000devpac", "algol68", "autoconf", "autohotkey", "awk",
	"cuesheet", "chaiscript", "clojure", "cpp-qt", "e",
	"ecmascript", "f1", "fsharp", "gambas", "gdb",
	"genie", "go", "gwbasic", "hicest", "icon",
	"j", "jquery", "lb", "logtalk", "magiksf",
	"mapbasic", "mmix", "modula2", "newlisp", "objecl",
	None, "oxygene", "oz", "pcre", "perl6",
	"pf", "pike", "postgresql", "powerbuilder", "purebasic",
	"q", "rpmspec", "rplus", "systemverilog", None,
	"unicon", "vala", "xbasic", "zxbasic", "uscript",
	"html5", "proftpd", "bascomavr", "c_loadrunner", "coffeescript",
	"epc", "falcon", "llvm", "pycon", "yalm",
	"freeswitch", None, None, None, None,
	None, None, None, None, None,
	None, "arm", "asymptote", "dcl", "dcpu16",
	"haxe", "ldif", "nagios", "octave", "parasail",
	"parigp", "pys60", "rexx", "spark", "sparql",
	"stonescript", "upc", "urbi", "vedit", None,
	"aimms", "chapel", "dart", "easytrieve", "ispf",
	"jcl", "nginx", "nim", "postscript", "qml",
	"racket", "rbscript", "rust", "scl", "standardml",
	"vbs", "c_winapi", "cpp-winapi", "netrexx", "json",
	"swift", "supercollider", "julia", "blitz3d", "blitzmax",
	"sqf", "puppet", "filemaker", "euphoria", "pli",
	"oorexx", "markdown", "kotlin", "ceylon", "arduino"
	]

def login(username, password):
	global logged
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
		logged = True
		return True
	for i in range(1, 7):
		if br.geturl() == "https://pastebin.com/login.php?e="+str(i):
			return False
	else:
		return False

def logout():
	global logged
	if logged:
		try:
			br.open("https://pastebin.com/logout")
			logged = False
			return True
		except Exception:
			return False
	else:
		return False

def paste(content, name="", expire="N", exposure=0, formatting=1):
	if formatting is None:
		formatting = 1
	if formatting in format_values:
		formatting = format_values.index(formatting)
#	if exposure == "":
#		exposure = 0
	if exposure in exposure_values:
		exposure = exposure_values.index(exposure)
	br.open("https://pastebin.com/")
	br.select_form("myform")
	br["paste_code"] = content
	br["paste_format"] = [str(formatting)]
	br["paste_expire_date"] = [expire]
	br["paste_private"] = [str(exposure)]
	br["paste_name"] = name
	br.submit()
	return br.geturl()

def user_list(username, result_limit=None):
	soup = BeautifulSoup(urlopen("https://pastebin.com/u/"+username), features="html5lib")
	content = []
	table = soup.find('table', attrs={'class':'maintable'})
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')

	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols][:-1]

		for a in row.find_all('a', href=True)[:-1]:
			if a.text:
				cols.insert(0, a['href'][1:])

		content.append([ele for ele in cols if ele])

	content = content[1:]
	if result_limit != None:
		del content[result_limit:len(content)]

	return content

def user_details(username):
	soup = BeautifulSoup(urlopen("https://pastebin.com/u/"+username), features="lxml")
	details = soup.find("div", {"class":"paste_box_line_u2"})
	content = []
	content.append((details.find_all("img", {"class":"t_vi"})[0].next_sibling).replace(' ', ''))
	content.append((details.find_all("img", {"class":"t_vi"})[1].next_sibling).replace(' ', ''))
	content.append(details.find("span").text)
	content.append(soup.find("img", {"class":"i_gb"}).get("src"))
	return content

def paste_details(key):
	soup = BeautifulSoup(urlopen("https://pastebin.com/"+key), features="lxml")
	details = soup.find("div", {"class":"paste_box_line2"})
	content = []
	content.append(soup.find("h1").text)
	content.append(details.find_all("a")[0].text)
	content.append(details.find("span").text)
	content.append((details.find("img", {"class":"t_ex"}).next_sibling)[:-4].replace(' ', ''))
	content.append((details.find("img", {"class":"t_vi"}).next_sibling)[:-5].replace(' ', ''))
	content.append(soup.find_all("a", {"class":"buttonsm"})[6].text)
	content.append((soup.find("span", {"class":"h_640"}).next_sibling)[:-4].replace(' ', ''))
	return content

def paste_content(key):
	content = urlopen("https://pastebin.com/raw/"+key).read()
	content = content.decode("utf-8")
	return content

def paste_delete(key):
	if logged:
		try:
			br.open("https://pastebin.com/delete/"+key)
			return True
		except Exception:
			return False
	else:
		return False

def profile_details():
	soup = BeautifulSoup(br.open("https://pastebin.com/profile"), features="lxml")
	content = []
	form = soup.find("form", {"id":"myform"})
	content.append((form.find_all("div", {"class":"form_right"})[0].text)[:-16][6:])
	content.append(form.find_all("input")[2].get("value"))
	content.append(form.find_all("input")[3].get("value"))
	content.append(form.find_all("input")[4].get("value"))
	content.append(form.find_all("img")[0].get("src"))
	return content
