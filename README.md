# simple-pastebin-wrapper
📝 Simple pastebin unofficial wrapper based on web automations.

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

account = pastebin.login("username", "password")
if account:
  print("Logged in !")
```
`login(username, password)`

- `username`
- `password`

---

### `logout()`

```py
import simple_pastebin as pastebin

account = pastebin.login("username", "password")
l = pastebin.logout()
if l:
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

- `content`
  - Paste content
  
**Optional**

- `name`
  - Paste title (optional)
  - Default `""`
- `expire`
  - Paste expiration date (optional)
  - Default `"N"`

| Value | Description |
|---|---|
| `"N"` | Never |
| `"10M"` | 10 minutes |
| `"1H"` | 1 hour |
| `"1D"` | 1 day |
| `"1W"` | 1 week |
| `"2W"` | 2 weeks |
| `"1M"` | 1 month |
| `"6M"` | 6 months |
| `"1Y"` | 1 year |

- `exposure`
  - Paste exposure status (optional)
  - Default `"0"`

| Value | Description |
|---|---|
| `"0"` | Public (default) |
| `"1"` | Unlisted |
| `"2"` | Private (members only) |

- `formatting`
  - Paste code formatting (optional)
  - Default `"1"`

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
