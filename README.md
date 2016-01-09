# gmaps-url-parser
![Build](https://travis-ci.org/walidsa3d/gmaps-url-parser.svg?branch=master)
![downloads](https://img.shields.io/pypi/dm/gmaps-url-parser.svg)
![license](https://img.shields.io/pypi/l/gmaps-url-parser.svg)
![version](https://img.shields.io/pypi/v/gmaps-url-parser.svg)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Parse google maps URLs

## Install (automatic)
```
$ pip install gmaps-url-parser
```
## Install (manual)
```
$ git clone 
$ cd gmaps-url-parser
$ python setup.py install
```
## Usage

```python
>>> from gmaps_url_parser import parse
>>> url = "https://www.google.com/maps/place/u+Saada,+Algeria/@35.2131065,4.1479717,10106m/data=!3m1!1e3!4m2!3m1!1s0x128bb3c644644ec3:0x7f746dd09dad9a9f"
>>> parse(url)
{'latitude': 35.2131065, 'zoom_level': '10106', 'place': 'Bou Saada, Algeria', 'maptype': 'earth', 'longitude': 4.1479717}
```
## License
MIT