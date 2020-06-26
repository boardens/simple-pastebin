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
pastebin.paste("Hello world")
```

## Documentation

### Overview

| Name | Type | Arguments | Description |
|---|---|---|---|
| `login` | Boolean | `username`, `password` | Login to a specific pastebin account, return operation status. |
| `logout` | Boolean | n/a | Logout from current account, return operation status. |
| `paste` | String | `content`, `name`, `expire`, `exposure`, `formatting` | Publish a paste, return url. |

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

### `logout()`

```py
import simple_pastebin as pastebin

account = pastebin.login("username", "password")
l = pastebin.logout()
if l:
  print("Logged out !")
```

### `paste()`

```py
import simple_pastebin as pastebin

p = pastebin.paste("Hello world", "title", expire="10M")
print(p)
```
`paste(content, name, expire, exposure, formatting)`

- `content`
- `name` (optional)
- `expire` (optional)
- `exposure` (optional)
- `formatting` (optional)

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
