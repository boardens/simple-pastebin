# simple-pastebin-wrapper
🧷 Simple pastebin unofficial wrapper based on web automations.

> Interact with pastebin without any API key or token.

- Paste, either logged in or anonymously
- 200+ selectable languages for syntax highlighting
- Set expiry times on pastes
- Set public/private/unlisted status for pastes

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
```
```py
# create your first paste
pastebin.paste("Hello world")
```

## Documentation

### Overview

| Name | Type | Arguments | Description |
|---|---|---|---|
| `login` | Boolean | `username`, `password` | Login to a specific pastebin account, return operation status. |
| `logout` | Boolean | n/a | Logout from current account, return operation status. |
| `paste` | String | `content`, `name`, `expire`, `exposure`, `formatting` | Publish a paste, return url. |

---

### `login()`

```py
import simple_pastebin as pastebin

log = pastebin.login("username", "password")
if log:
  print("Logged in !")
```
`login(username, password)`

- `username` (string)
- `password` (string)

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

### `paste()`

```py
import simple_pastebin as pastebin

p = pastebin.paste("Hello world", "title", expire="10M")
print(p)
```
`paste(content, name, expire, exposure, formatting)`

> Note : if you create a paste without logging in, it will be anonymous.

- `content` (string)
  - Paste content
  
**Optional**

- `name` (string)
  - Paste title
- `expire` (string from list)
  - Paste expiration date

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

- `exposure` (string from list)
  - Paste exposure status

| Id | Value | Description |
|---|---|---|
| `"0"` | `"public"` | Public (default) |
| `"1"` | `"unlisted"` | Unlisted |
| `"2"` | `"private"` | Private (members only) |

- `formatting` (string from list)
  - Paste code formatting

| Id | Value | Description |
|---|---|---|
| `"1"` | `"none"` | None (default) |

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

## Implementations

Currently working on other major implementations like :
- hiding multiples automations and preventing captcha security behind proxies
- improving and simplifying functions argumentations
- adding paste gestion for connected members

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
