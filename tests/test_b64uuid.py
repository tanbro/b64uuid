from itertools import combinations
from random import choice
from unittest.case import TestCase
from urllib.parse import quote
from uuid import uuid1, uuid4

from b64uuid import B64Uuid, b64sid_to_uuid, uuid_to_b64sid


class B64UuidTestCase(TestCase):
    def test_initial(self):
        for _ in range(100):
            uid = choice([uuid1(), uuid4()])
            id_list = [
                uid,
                B64Uuid(uid),
                B64Uuid(uid.bytes),
                B64Uuid(uid.int),
                B64Uuid(uid.hex),
                B64Uuid(str(uid)),
            ]
            id_list.append(B64Uuid(choice(id_list[1:]).string))  # from b64id string
            for a, b in combinations(id_list, 2):
                self.assertEqual(a, b)

    def test_string_length(self):
        for _ in range(100):
            b64id = B64Uuid()
            self.assertEqual(len(b64id.string), 22)
        for _ in range(100):
            b64id = B64Uuid(uuid1())
            self.assertEqual(len(b64id.string), 22)

    def test_urlsafe(self):
        for _ in range(100):
            b64id = B64Uuid()
            self.assertEqual(quote(b64id.string), b64id.string)

    def test_equal_uuid(self):
        for _ in range(100):
            uid = choice([uuid1(), uuid4()])
            b64id = B64Uuid(uid)
            self.assertEqual(b64id, uid)
            self.assertEqual(b64id.uuid, uid)


class StrToUuidTestCase(TestCase):
    def test_str2uuid(self):
        size = 100
        uuid_list = [choice([uuid1(), uuid4()]) for _ in range(size)]
        b64str_list = [B64Uuid(m).string for m in uuid_list]
        for uid, s in zip(uuid_list, b64str_list):
            uid1 = b64sid_to_uuid(s)
            self.assertEqual(uid, uid1)


class UuidToStrTestCase(TestCase):
    def test_str2uuid(self):
        size = 100
        uuid_list = [choice([uuid1(), uuid4()]) for _ in range(size)]
        b64id_list = [B64Uuid(m) for m in uuid_list]
        for uid, bid in zip(uuid_list, b64id_list):
            sid = uuid_to_b64sid(uid)
            self.assertEqual(sid, bid.string)
