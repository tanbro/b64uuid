# b64uuid

---

[![pytest](https://github.com/tanbro/b64uuid/workflows/pytest/badge.svg)](https://github.com/tanbro/b64uuid/actions?query=workflow%3Apytest)
[![PyPI](https://img.shields.io/pypi/v/b64uuid.svg)](https://pypi.org/project/b64uuid)
[![Documentation Status](https://readthedocs.org/projects/b64uuid/badge/?version=latest)](https://b64uuid.readthedocs.io/en/latest/?badge=latest)

---

A small Python library and command-line tool to encode/decode UUID to/from a 22 characters shorter URL safe base64 string.

We can use it to make UUID string a little shorter.

## Installation

- Installing from [PyPI](https://pypi.org/):

  ```bash
  pip install b64uuid
  ```

- Installing from a local src tree:

  ```bash
  pip install .
  ```

  or

  ```bash
  python setup.py install
  ```

Check <https://packaging.python.org/tutorials/installing-packages> for more details.

## Command Line Usages

- Make a random short ID

  ```bash
  $ b64uuid
  bxntPh4PSA6-OMDfBXMLhQ
  ```

- Short ID from UUID

  ```sh
  $ b64uuid -u 2863a16d-b6ae-45a2-9d74-98d20377d56a
  KGOhbbauRaKddJjSA3fVag
  ```

- Short ID to UUID

  ```sh
  $ b64uuid -s KGOhbbauRaKddJjSA3fVag
  2863a16d-b6ae-45a2-9d74-98d20377d56a
  ```

## Library Usages

- Make a random short ID

  ```python
  >>> from b64uuid import B64UUID
  >>>
  >>> B64UUID().string
  'Ft018l4aTwalxqDHMQoqTQ'
  ```

- Short ID from UUID

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

- Short ID to UUID

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
