<h2>Ham-or-Spam</h2>

[![Requirements Status](https://requires.io/github/inderpartap/ham-or-spam/requirements.svg?branch=master)](https://requires.io/github/inderpartap/ham-or-spam/requirements/?branch=master)
<br>
[![Build Status](https://travis-ci.org/inderpartap/ham-or-spam.svg?branch=master)](https://travis-ci.org/inderpartap/ham-or-spam)

> An intelligent spam filtering system built using a **custom Naive Bayes classifier**

**:arrow_forward: You can try it out here at [https://ham-or-spam.herokuapp.com/](https://ham-or-spam.herokuapp.com/)**

***

## Table of contents

- [REST API usage](#rest-api-usage)
    - [using `curl`](#using-curl)
    - [using `requests` (python)](#using-requests)
    - [using standard python 3 library](#using-standard-python-3-library)
- [Technologies used](#technologies-used)
    - [Backend](#backend)
    - [Front end](#front-end)
- [Contributing](#contributing)
    - [Installing it locally](#installing-it-locally)
    - [Running it](#running-it)
    - [Contributers](#contributers)
- [FAQ](#faq)
    - [What is the classifier based on](#what-is-the-classifier-based-on)
    - [What did you train the classifier on](#what-did-you-train-the-classifier-on)
    - [How accurate is it](#how-accurate-is-it)
- [Roadmap](#roadmap)
- [Legal stuff](#legal-stuff)

***

## REST API usage
[:arrow_up: Back to top](#table-of-contents)

Yes, we do provide an **API** for our service!

#### using `curl`

**General Syntax**

```bash
$ curl -H "Content-Type: application/json" -X \
POST -d \
'{"email_text":"SAMPLE EMAIL TEXT"}' \
https://ham-or-spam.herokuapp.com/api/v1/classify/
```

**Show me an example**

You thought I was lying!

```bash
$ curl -H "Content-Type: application/json" \
-X POST -d \
'{"email_text":"Dear Inderpartap, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman"}' \
https://ham-or-spam.herokuapp.com/api/v1/classify/
```

**JSON response**

```python
{
  "email_class": "spam", 
  "email_text": "Dear Inderpartap, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman", 
  "status": 200
}
```

#### using `requests`
[:arrow_up: Back to top](#table-of-contents)


```python
>>> import requests
>>> import json
>>> import pprint
>>>
>>> api_url = "https://ham-or-spam.herokuapp.com/api/v1/classify/"
>>> payload = \
{
'email_text': 'Dear Inderpartap, I would like to immediately transfer 10000 '
               'thousand dollars to your account as my beloved husband has '
               'expired and I have nobody to ask for to transfer the money '
               'to your account. I come from the family of the royal prince '
               'of burkino fasa and I would be more than obliged to take '
               'your help on this matter. Would you care to share your bank '
               'account details with me in the next email conversation that '
               'we have? -regards -Liah herman'
}
>>>
>>> headers = {'content-type': 'application/json'}
>>> # query our API
>>> response = requests.post(api_url, data=json.dumps(payload), headers=headers)
>>> response.status_code
200
>>> pprint.pprint(response.json())
{
 'email_class': 'spam',
 'email_text': 'Dear Inderpartap, I would like to immediately transfer 10000 '
               'thousand dollars to your account as my beloved husband has '
               'expired and I have nobody to ask for to transfer the money '
               'to your account. I come from the family of the royal prince '
               'of burkino fasa and I would be more than obliged to take '
               'your help on this matter. Would you care to share your bank '
               'account details with me in the next email conversation that '
               'we have? -regards -Liah herman',
 'status': 200
 }
>>> 
```

#### Using standard python 3 library
[:arrow_up: Back to top](#table-of-contents)

[requests module](https://github.com/kennethreitz/requests) really makes our life easy and I use it all the time. But **sigh**, there should be an example using the standard library so here it is

```python
>>> import urllib.request
>>> import json
>>> import pprint 
>>>
>>> url = "https://ham-or-spam.herokuapp.com/api/v1/classify/"
>>> req = urllib.request.Request(url)
>>> req.add_header(
       'Content-Type',
       'application/json; charset=utf-8'
   )
>>>
>>> body = \
{'email_text': 'Dear Inderpartap, I would like to immediately transfer 10000 '
               'thousand dollars to your account as my beloved husband has '
               'expired and I have nobody to ask for to transfer the money '
               'to your account. I come from the family of the royal prince '
               'of burkino fasa and I would be more than obliged to take '
               'your help on this matter. Would you care to share your bank '
               'account details with me in the next email conversation that '
               'we have? -regards -Liah herman'
}
>>> json_data = json.dumps(body).encode('utf-8')   # needs to be bytes
>>> req.add_header('Content-Length', len(json_data))
>>>
>>> with urllib.request.urlopen(req, json_data) as f:
...   print(f.read().decode('utf-8'))
... 
{
  "email_class": "spam", 
  "email_text": "Dear Inderpartap, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman", 
  "status": 200
}
>>> 
```

***

## Technologies used
[:arrow_up: Back to top](#table-of-contents)

Built upon the giant shoulders of (__in no particular order__)

#### Backend

- [Flask](http://flask.pocoo.org/) because __I ♥ `Flask` more than [`Django`](https://www.djangoproject.com/)__
- [Flask-Cache](https://pythonhosted.org/Flask-Cache/) for **caching**
- [nltk](http://nltk.org) for text pre-processing
- [gunicorn](http://gunicorn.org/) as the production server
- [Jinja2](http://jinja.pocoo.org/) as the templating engine
- [dill](https://pypi.python.org/pypi/dill) for de-serializing complex python objects

[and some more](https://github.com/inderpartap/ham-or-spam/blob/master/requirements.txt)

#### Front end

- [MaterializeCSS](http://materializecss.com/)
- [Jquery](https://jquery.com/)
- [WowJS](https://github.com/matthieua/WOW)

***

## Testing
[:arrow_up: Back to top](#table-of-contents)

#### Installing it locally

```bash
$ virtualenv env              # Create virtual environment
$ source env/bin/activate     # Change default python to virtual one
(env)$ git clone https://github.com/inderpartap/ham-or-spam.git
(env)$ cd ham-or-spam
(env)$ pip install -r requirements.txt
```

#### Running it

```sh
$ make run
```


#### Contributers

- [Raghav Kakkar (rkakkar7)](https://github.com/rkakkar7) : **UI dev**
- [Sudhanva Devanathan (agreedplains3)](https://github.com/agreedplains3): **Test cases**

***

## Roadmap
[:arrow_up: Back to top](#table-of-contents)

- [x] Deploying to heroku
- [x] Creating a REST API
- [x] Improving the UI
- [x] Writing tests
- [ ] Simple API authentication
