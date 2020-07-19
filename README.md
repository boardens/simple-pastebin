# simple-pastebin
🧷 Simple pastebin unofficial wrapper based on web automations.

> Interact with pastebin without any API key or token.<br>
> Lightweight alternative to [PyPI Pastebin API](https://pypi.org/project/Pastebin/).

### Features

- Paste, either logged in or anonymously
- 200+ selectable languages for syntax highlighting
- Set expiry times on pastes
- Set public/private/unlisted status for pastes
- See trending/recents pastes
- See pastes by a particular user
- Delete your pastes
- Retrieve your user details

## Get started

**Note** : Python 3.6 or higher is required.

```bash
# clone the repository
$ git clone https://github.com/boardens/simple-pastebin.git

# change the working directory to simple-pastebin
$ cd simple-pastebin

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Installation

> Install the package by running setup file.

```bash
# install package
$ python3 setup.py install

# check if package is correctly installed
$ python3 -m pip show simple_pastebin
```

### Usage

> Learn about usage by reading [documentation](/DOCUMENTATION.md).

```py
# import library
import simple_pastebin as pastebin

# create your first paste
pastebin.paste("Hello world")
```

## Implementations

Currently working on other major implementations like :
- Hiding multiples automations and preventing captcha security behind proxies
- Improving and simplifying functions argumentations (especially ids and values)
- Adding paste gestion for connected members

## Legal

**Disclaimer**: This is not affliated, endorsed or certified in any way by Pastebin.<br>
This is an independent and unofficial work. Strictly not for spam. Use at your own risk.

## License

[GPL-3.0](https://github.com/boardens/watson/LICENSE/) License
