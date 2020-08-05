from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Union
from uuid import UUID, uuid4

__all__ = ['B64Uuid', 'b64uuid_str_to_uuid']


class B64Uuid:
    def __init__(self, uuid: Union[None, UUID, str, bytes, int] = None):
        if uuid is None:
            self._uuid = uuid4()
        elif isinstance(uuid, UUID):
            self._uuid = uuid
        elif isinstance(uuid, str):
            if len(uuid) < 32:
                self._uuid = UUID(bytes=urlsafe_b64decode(uuid.rstrip('=') + '=='))
            else:
                self._uuid = UUID(hex=uuid)
        elif isinstance(uuid, bytes):
            self._uuid = UUID(bytes=uuid)
        elif isinstance(uuid, int):
            self._uuid = UUID(int=uuid)
        else:
            raise TypeError(f'Can not convert `uuid` parameter from {type(uuid)} to {UUID}')
        data = urlsafe_b64encode(self._uuid.bytes).rstrip(b'=')
        self._string = data.decode('ascii')

    def __str__(self):
        return self._string

    def __repr__(self):
        return '<{} object at 0x{:x} string={}>'.format(
            self.__class__.__qualname__, id(self), self._string
        )

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def string(self) -> str:
        return self._string


def b64uuid_str_to_uuid(s: str) -> UUID:
    return UUID(bytes=urlsafe_b64decode(s.rstrip('=') + '=='))
