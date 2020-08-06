# b64uuid

---

[![pytest](https://github.com/tanbro/b64uuid/workflows/pytest/badge.svg)](https://github.com/tanbro/b64uuid/actions?query=workflow%3Apytest)
[![PyPI](https://img.shields.io/pypi/v/b64uuid.svg)](https://pypi.org/project/b64uuid/)

---

A small Python library and command-line tool to encode/decode UUID to/from a 22 characters shorter URL safe base64 string.

We can use it to make UUID string a little shorter.

## Installation

- Install from PyPI:

  ```bash
  pip install b64uuid
  ```

- Install from source :

  Clone or download whole project, enter the project's root directory, then

  ```bash
  pip install -e .
  ```

  or

  ```bash
  python setup.py install
  ```

Check <https://packaging.python.org/tutorials/installing-packages/> for more details.

## Command Line Usage

- Make a random short ID

  ```bash
  $ b64uuid
  bxntPh4PSA6-OMDfBXMLhQ
  ```

- Short ID from UUID

  ```bash
  $ b64uuid -u 2863a16d-b6ae-45a2-9d74-98d20377d56a
  KGOhbbauRaKddJjSA3fVag
  ```

- Short ID to UUID

  ```bash
  $ b64uuid -s KGOhbbauRaKddJjSA3fVag
  2863a16d-b6ae-45a2-9d74-98d20377d56a
  ```

## Library Usage

- Shorten UUID string

  ```python
  >>> from uuid import uuid1
  >>> from b64uuid import B64UUID
  >>>
  >>> uid = uuid1()
  >>> str(uid)
  'cb6e319c-d793-11ea-9619-1cb72cde3f7f'
  >>> bid = B64UUID(uid)
  >>> str(bid)
  'y24xnNeTEeqWGRy3LN4_fw'
  ```

- Generate a new short ID

  ```python
  >>> from b64uuid import B64UUID
  >>>
  >>> B64UUID().string
  'Ft018l4aTwalxqDHMQoqTQ'
  ```

- Restore UUID from short ID

  ```python
  >>> from uuid import uuid1
  >>> from b64uuid import B64UUID
  >>>
  >>> uid = uuid1()
  >>> uid.hex
  '95327416d79411ea96191cb72cde3f7f'
  >>> short_id = B64UUID(uid).string
  >>> short_id
  'lTJ0FteUEeqWGRy3LN4_fw'
  >>> B64UUID(short_id).uuid.hex
  '95327416d79411ea96191cb72cde3f7f'
  ```
