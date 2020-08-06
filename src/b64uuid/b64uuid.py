from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Union
from uuid import UUID, uuid4

__all__ = ['b64sid_to_uuid', 'uuid_to_b64sid', 'B64UUID']


def b64sid_to_uuid(s: str) -> UUID:
    return UUID(bytes=urlsafe_b64decode(s.rstrip('=') + '=='))


def uuid_to_b64sid(value: UUID) -> str:
    return B64UUID(value).string


class B64UUID:
    def __init__(self, initial: Union[None, UUID, str, bytes, int] = None):
        if initial is None:
            self._uuid = uuid4()
        elif isinstance(initial, UUID):
            self._uuid = initial
        elif isinstance(initial, str):
            if len(initial) < 32:
                self._uuid = b64sid_to_uuid(initial)
            else:
                self._uuid = UUID(hex=initial)
        elif isinstance(initial, bytes):
            self._uuid = UUID(bytes=initial)
        elif isinstance(initial, int):
            self._uuid = UUID(int=initial)
        else:
            raise TypeError(
                'Can not convert initial value from type {} to {}'.format(
                    type(initial), UUID
                )
            )
        self._string = urlsafe_b64encode(self._uuid.bytes).rstrip(b'=').decode('ascii')

    def __str__(self):
        return self._string

    def __repr__(self):
        return '<{} object at 0x{:x} string={!r}>'.format(
            self.__class__.__qualname__, id(self), self._string
        )

    def __lt__(self, other):
        if isinstance(other, UUID):
            return self.uuid < other
        return self.uuid < other.uuid

    def __le__(self, other):
        if isinstance(other, UUID):
            return self.uuid <= other
        return self.uuid <= other.uuid

    def __eq__(self, other):
        if isinstance(other, UUID):
            return self.uuid == other
        return self.uuid == other.uuid

    def __ne__(self, other):
        if isinstance(other, UUID):
            return self.uuid != other
        return self.uuid != other.uuid

    def __gt__(self, other):
        if isinstance(other, UUID):
            return self.uuid > other
        return self.uuid > other.uuid

    def __ge__(self, other):
        if isinstance(other, UUID):
            return self.uuid >= other
        return self.uuid >= other.uuid

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def string(self) -> str:
        return self._string
