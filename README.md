# simple-pastebin-wrapper
🧷 Simple pastebin unofficial wrapper based on web automations.

> Interact with pastebin without any API key or token.<br>
> Lightweight alternative to [PyPI Pastebin API](https://pypi.org/project/Pastebin/).

- Paste, either logged in or anonymously
- 200+ selectable languages for syntax highlighting
- Set expiry times on pastes
- Set public/private/unlisted status for pastes
- See pastes by a particular user

### Soonly added

- See trending/recents pastes
- Delete your pastes
- Retrieve your user details

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# clone the repository
$ git clone https://github.com/boardens/simple-pastebin-wrapper.git

# change the working directory to simple-pastebin-wrapper
$ cd simple-pastebin-wrapper

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Installation

> Currently working on a setup file to facilitate installation.

```bash
# get site-packages directory
$ python3 -m site --user-site

# copy script to site-packages directory
$ cp simple_pastebin.py {site-packages}
```

### Usage

```py
# import library
import simple_pastebin as pastebin

# create your first paste
pastebin.paste("Hello world")
```

## Documentation

### Overview

| Name | Type | Arguments | Description |
|---|---|---|---|
| [`login`](#login) | Boolean | `username` `password` | Login to a specific pastebin account, return operation status. |
| [`logout`](#logout) | Boolean | n/a | Logout from current account, return operation status. |
| [`user_list`](#user_list) | String (list) | `username` `result_limit` | List all pastes by username, return list. |
| [`paste_details`](#paste_details) | String (list) | `key` | List all details by paste, return list. |
| [`paste_content`](#paste_content) | String | `key` | Get paste raw content, return content. |
| [`paste`](#paste) | String | `content` `name` `expire` `exposure` `formatting` | Publish a paste, return url. |

---

### `login()`

```py
import simple_pastebin as pastebin

log = pastebin.login("username", "password")
if log:
  print("Logged in !")
```
`login(username, password)`

| Argument | Type | Description |
|---|---|---|
| `username` | String | Pastebin account username. |
| `password` | String | Pastebin account password. |

---

### `logout()`

```py
import simple_pastebin as pastebin

log = pastebin.login("username", "password")
exit = pastebin.logout()
if exit:
  print("Logged out !")
```
`logout()`

---

### `user_list()`

```py
import simple_pastebin as pastebin

list = pastebin.user_list("username", result_limit=5)
print(list)
```
`user_list(username, result_limit)`

| Argument | Type | Description |
|---|---|---|
| `username` | String | Pastebin account username. |

#### Optional

| Argument | Type | Description |
|---|---|---|
| `result_limit` | Integer | Paste result return limit. |

#### Output

```bash
# Output as list format :
[[key, name, date, expire, hits, formatting], ...]
```

---

### `paste_details()`

```py
import simple_pastebin as pastebin

list = pastebin.paste_details("kJApGqbK")
print(list)
```
`paste_details(key)`

| Argument | Type | Description |
|---|---|---|
| `key` | String | Paste url key. |

#### Output

```bash
# Output as list format :
[[name, username, date, expire, hits, formatting, size], ...]
```

---

### `paste_content()`

```py
import simple_pastebin as pastebin

content = pastebin.paste_content("kJApGqbK")
print(content)
```
`paste_content(key)`

| Argument | Type | Description |
|---|---|---|
| `key` | String | Paste url key. |

---

### `paste()`

```py
import simple_pastebin as pastebin

p = pastebin.paste("Hello world", "title", expire="10M")
print(p)
```
`paste(content, name, expire, exposure, formatting)`

> Note : if you create a paste without logging in, it will be anonymous.

| Argument | Type | Description |
|---|---|---|
| `content` | String | Paste content. |

#### Optional

| Argument | Type | Description |
|---|---|---|
| `name` | String | Paste title. |
| `expire` | String | Paste expiration delay. |
| `exposure` | Integer, string | Paste exposure status. |
| `formatting` | Integer, string | Paste code formatting. |

#### Valid `expire` values

> get `expire_values`

| Value | Description |
|---|---|
| `"N"` | Never (default) |
| `"10M"` | 10 minutes |
| `"1H"` | 1 hour |
| `"1D"` | 1 day |
| `"1W"` | 1 week |
| `"2W"` | 2 weeks |
| `"1M"` | 1 month |
| `"6M"` | 6 months |
| `"1Y"` | 1 year |

#### Valid `exposure` values and ids

> get `exposure_values`

| Id | Value | Description |
|---|---|---|
| `0` | `"public"` | Public (default) |
| `1` | `"unlisted"` | Unlisted |
| `2` | `"private"` | Private (members only) |

#### Valid `formatting` values and ids

> get `format_values`

| Id | Value | Description |
|---|---|---|
| `1` | `"text"` | None (default) |
| `142` | `"4cs"` | 4CS |
| `143` | `"6502acme"` | 6502 ACME Cross Assembler |
| `144` | `"6502kickass"` | 6502 Kick Assembler |
| `145` | `"6502tasm"` | 6502 TASM/64TASS |
| `73` | `"abap"` | ABAP |
| `2` | `"actionscript"` | ActionScript |
| `74` | `"actionscript3"` | ActionScript 3 |
| `3` | `"ada"` | Ada |
| `236` | `"aimms"` | AIMMS |
| `147` | `"algol68"` | ALGOL 68 |
| `4` | `"apache"` | Apache Log |
| `5` | `"applescript"` | AppleScript |
| `75` | `"apt_sources"` | APT Sources |
| `270` | `"arduino"` | Arduino |
| `217` | `"arm"` | ARM |
| `6` | `"arm_nasm"` | ARM (NASM) |
| `7` | `"asp"` | ASP |
| `218` | `"asymptote"` | Asymptote |
| `148` | `"autoconf"` | autoconf |
| `149` | `"autohotkey"` | Autohotkey |
| `54` | `"autolt"` | Autolt |
| `76` | `"avisynth"` | Avisynth |
| `150` | `"awk"` | Awk |
| `198` | `"bascomavr"` | BASCOM AVR |
| `8` | `"bash"` | Bash |
| `77` | `"basic4gl"` | Basic4GL |
| `20` | `"batch"` | Batch |
| `78` | `"bibtex"` | BibTeX |
| `55` | `"blitzbasic"` | Blitz Basic |
| `259` | `"blitz3d"` | Blitz3D |
| `260` | `"blitzmax"` | BlitzMax |
| `56` | `"bnf"` | BNF |
| `80` | `"boo"` | BOO |
| `79` | `"bf"` | BrainFuck |
| `9` | `"c"` | C |
| `252` | `"c_winapi"` | C (WinAPI) |
| `10` | `"c_mac"` | C for Macs |
| `82` | `"cil"` | C intermediate Language |
| `14` | `"csharp"` | C# |
| `13` | `"cpp"` | C++ |
| `253` | `"cpp-winapi"` | C++ (WinAPI) |
| `154` | `"cpp-qt"` | C++ (with Qt extensions) |
| `199` | `"c_loadrunner"` | C: Loadrunner |
| `11` | `"caddcl"` | CAD DCL |
| `12` | `"cadlisp"` | CAD Lisp |
| `269` | `"ceylon"` | Ceylon |
| `81` | `"cfdg"` | CFDG |
| `152` | `"chaiscript"` | ChaiScript |
| `237` | `"chapel"` | Chapel |
| `153` | `"clojure"` | Clojure |
| `99` | `"klonec"` | Clone C |
| `100` | `"klonecpp"` | Clone C++ |
| `83` | `"cmake"` | CMake |
| `84` | `"cobol"` | COBOL |
| `200` | `"coffeescript"` | CoffeeScript |
| `15` | `"coldfusion"` | ColdFusion |
| `16` | `"css"` | CSS |
| `151` | `"cuesheet"` | Cuesheet |
| `17` | `"d"` | D |
| `238` | `"dart"` | Dart |
| `219` | `"dcl"` | DCL |
| `220` | `"dcpu16"` | DCPU-16 |
| `85` | `"dcs"` | DCS |
| `18` | `"delphi"` | Delphi |
| `177` | `"oxygene"` | Delphi Prism (Oxygene) |
| `19` | `"diff"` | Diff |
| `86` | `"div"` | DIV |
| `87` | `"dot"` | DOT |
| `155` | `"e"` | E |
| `239` | `"easytrieve"` | Easytrieve |
| `156` | `"ecmascript"` | ECMAScript |
| `21` | `"eiffel"` | Eiffel |
| `88` | `"email"` | Email |
| `201` | `"epc"` | EPC |
| `57` | `"erlang"` | Erlang |
| `264` | `"euphoria"` | Euphoria
| `158` | `"fsharp"` | F# |
| `202` | `"falcon"` | Falcon |
| `263` | `"filemaker"` | Filemaker |
| `89` | `"fo"` | FO Language |
| `157` | `"f1"` | Formula One |
| `22` | `"fortran"` | Fortran |
| `23"` | `"freebasic"` | FreeBasic |
| `206` | `"freeswitch"` | FreeSWITCH |
| `159` | `"gambas"` | GAMBAS |
| `24` | `"gml"` | Game Maker |
| `160` | `"gdb"` | GDB |
| `58` | `"genero"` | Genero |
| `161` | `"genie"` | Genie |
| `90` | `"gettext"` | GetText |
| `162` | `"go"` | Go |
| `59` | `"groovy"` | Groovy |
| `163` | `"gwbasic"` | GwBasic |
| `60` | `"haskell"` | Haskell |
| `221` | `"haxe"` | Haxe |
| `164` | `"hicest"` | HicEst |
| `93` | `"hq9plus"` | HQ9 Plus |
| `25` | `"html4strict"` | HTML |
| `196` | `"html5"` | HTML5 |
| `165` | `"icon"` | Icon |
| `94` | `"idl"` | IDL |
| `26` | `"ini"` | INI file |
| `61` | `"inno"` | Inno Script |
| `95` | `"intercal"` | INTERCAL |
| `96` | `"io"` | IO |
| `240` | `"ispf"` | ISPF Panel Definition |
| `166` | `"j"` | J |
| `27` | `"java"` | Java |
| `97` | `"java5"` | Java 5 |
| `28` | `"javascript"` | JavaScript |
| `241` | `"jcl"` | JCL |
| `167` | `"jquery"` | jQuery |
| `255` | `"json"` | JSON |
| `258` | `"julia"` | Julia |
| `98` | `"kixtart"` | KiXtart |
| `268` | `"kotlin"` | Kotlin |
| `62` | `"latex"` | Latex |
| `222` | `"ldif"` | LDIF |
| `168` | `"lb"` | Liberty BASIC |
| `63` | `"lsl2"` | Linden Scripting |
| `29` | `"lisp"` | Lisp |
| `203` | `"llvm"` | LLVM |
| `101` | `"locobasic"` | Loco Basic |
| `169` | `"logtalk"` | Logtalk |
| `102` | `"lolcode"` | LOL Code |
| `103` | `"lotusformula"` | Lotus Formulas |
| `104` | `"lotusscript"` | Lotus Script |
| `105` | `"lscript"` | LScript |
| `30` | `"lua"` | Lua |
| `65` | `"m68k"` | M68000 Assembler |
| `170` | `"magiksf"` | MagikSF |
| `106` | `"make"` | Make |
| `171` | `"mapbasic"` | MapBasic |
| `267` | `"markdown"` | Markdown (PRO members only) |
| `64` | `"matlab"` | MatLab |
| `66` | `"mirc"` | mIRC |
| `172` | `"mmix"` | MIX Assembler |
| `173` | `"modula2"` | Modula 2 |
| `107` | `"modula3"` | Modula 3 |
| `146` | `"68000devpac"` | Motorola 68000 HiSoft Dev |
| `32` | `"mpasm"` | MPASM |
| `108` | `"mxml"` | MXML |
| `33` | `"mysql"` | MySQL |
| `223` | `"nagios"` | Nagios |
| `254` | `"netrexx"` | NetRexx |
| `174` | `"newlisp"` | newLISP |
| `242` | `"nginx"` | Nginx |
| `243` | `"nim"` | Nim |
| `34` | `"nsis"` | NullSoft Installer |
| `109` | `"oberon2"` | Oberon 2 |
| `175` | `"objecl"` | Objeck Programming Langua |
| `35` | `"objc"` | Objective C |
| `36` | `"ocaml"` | OCaml |
| `110` | `"ocaml_brief"` | OCaml Brief |
| `224` | `"octave"` | Octave |
| `266` | `"oorexx"` | Open Object Rexx |
| `181` | `"pf"` | OpenBSD PACKET FILTER |
| `91` | `"glsl"` | OpenGL Shading |
| `37` | `"oobas"` | Openoffice BASIC |
| `111` | `"oracle11"` | Oracle 11 |
| `38` | `"oracle8"` | Oracle 8 |
| `178` | `"oz"` | Oz |
| `225` | `"parasail"` | ParaSail |
| `226` | `"parigp"` | PARI/GP |
| `39` | `"pascal"` | Pascal |
| `141` | `"pawn"` | Pawn |
| `179` | `"pcre"` | PCRE |
| `112` | `"per"` | Per |
| `40` | `"perl"` | Perl |
| `180` | `"perl6"` | Perl 6 |
| `41` | `"php"` | PHP |
| `113` | `"php_brief"` | PHP Brief |
| `114` | `"pic16"` | Pic 16 |
| `182` | `"pike"` | Pike |
| `115` | `"pixelblender"` | Pixel Bender |
| `265` | `"pli"` | PL/I |
| `68` | `"plsql"` | PL/SQL |
| `183` | `"postgresql"` | PostgreSQL |
| `244` | `"postscript"` | PostScript |
| `116` | `"povray"` | POV-Ray |
| `184` | `"powerbuilder"` | PowerBuilder |
| `117` | `"powershell"` | PowerShell |
| `197` | `"proftpd"` | ProFTPd |
| `118` | `"progress"` | Progress |
| `119` | `"prolog"` | Prolog |
| `120` | `"properties"` | Properties |
| `121` | `"providex"` | Provide X |
| `262` | `"puppet"` | Puppet |
| `185` | `"purebasic"` | PureBasic |
| `204` | `"pycon"` | PyCon |
| `42` | `"python"` | Python |
| `227` | `"pys60"` | Python for S60 |
| `186` | `"q"` | q/kdb+ |
| `43` | `"qbasic"` | QBasic |
| `245` | `"qml"` | QML |
| `188` | `"rplus"` | R |
| `246` | `"racket"` | Racket |
| `67` | `"rails"` | Rails |
| `247` | `"rbscript"` | RBScript |
| `122` | `"rebol"` | REBOL |
| `123` | `"reg"` | REG |
| `228` | `"rexx"` | Rexx |
| `44` | `"robots"` | Robots |
| `187` | `"rpmspec"` | RPM Spec |
| `45` | `"ruby"` | Ruby |
| `92` | `"gnuplot"` | Ruby Gnuplot |
| `248` | `"rust"` | Rust |
| `124` | `"sas"` | SAS |
| `125` | `"scala"` | Scala |
| `46` | `"scheme"` | Scheme |
| `126` | `"scilab"` | Scilab |
| `249` | `"scl"` | SCL |
| `127` | `"sdlbasic"` | SdlBasic |
| `69` | `"smalltalk"` | Smalltalk |
| `47` | `"smarty"` | Smarty |
| `229` | `"spark"` | SPARK |
| `230` | `"sparql"` | SPARQL |
| `261` | `"sqf"` | SQF |
| `48` | `"sql"` | SQL |
| `250` | `"standardml"` | StandardML |
| `231` | `"stonescript"` | StoneScript |
| `257` | `"supercollider"` | SuperCollider |
| `256` | `"swift"` | Swift |
| `189` | `"systemverilog"` | SystemVerilog |
| `130` | `"tsql"` | T-SQL |
| `70` | `"tcl"` | TCL |
| `128` | `"terarerm"` | Tera Term |
| `129` | `"thinbasic"` | thinBasic |
| `131` | `"typoscript"` | TypoScript |
| `191` | `"unicon"` | Unicon |
| `195` | `"uscript"` | UnrealScript |
| `232` | `"upc"` | UPC |
| `233` | `"urbi"` | Urbi |
| `192` | `"vala"` | Vala |
| `51` | `"vbnet"` | VB.NET |
| `251` | `"vbs"` | VBScript |
| `234` | `"vedit"` | Vedit |
| `132` | `"verilog"` | VeriLog |
| `133` | `"vhdl"` | VHDL |
| `134` | `"vim"` | VIM |
| `135` | `"visualprolog"` | Visual Pro Log |
| `50` | `"vb"` | VisualBasic |
| `52` | `"visualprofox"` | VisualFoxPro |
| `136` | `"whitespace"` | WhiteSpace |
| `137` | `"whois"` | WHOIS |
| `138` | `"winbatch"` | Winbatch |
| `193` | `"xbasic"` | XBasic |
| `53` | `"xml"` | XML |
| `139` | `"xorg_conf"` | Xorg Config |
| `140` | `"xpp"` | XPP |
| `205` | `"yalm"` | YALM |
| `72` | `"z80"` | Z80 Assembler |
| `194` | `"zxbasic"` | ZXBasic |

> ⚠️ The following ids are not responding to any item :

> `0` `31` `49` `71` `176` `207` `208` `209` `210`<br>
> `211` `212` `213` `214` `215` `216` `235`

---

### Examples

```py
import simple_pastebin as pastebin

username = "username"
password = "password"

log = pastebin.login(username, password)

if log:
  print("Connected as "+username)
  print(pastebin.paste("Hello world", "title", expire="10M"))
  pastebin.logout()
```
```py
import simple_pastebin as pastebin

username = "username"
password = "password"

log = pastebin.login(username, password)

if log:
  print("Connected as "+username)
  list = pastebin.user_list(username)

  for i in range(len(list)):
    print(list[i][1])

  pastebin.logout()
```

## Implementations

Currently working on other major implementations like :
- Hiding multiples automations and preventing captcha security behind proxies
- Improving and simplifying functions argumentations (especially ids and values)
- Adding paste gestion for connected members

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
