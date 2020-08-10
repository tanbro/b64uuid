from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Union
from uuid import UUID, uuid4

__all__ = ['b64id_to_uuid', 'uuid_to_b64id', 'B64UUID']


def b64id_to_uuid(s: str) -> UUID:
    """Convert a Base64 URL safe ID string to an :class:`uuid.UUID` object

    Parameters
    ----------

    s : str
        The UUID string in Base64 url safe style

    Returns
    -------
    uuid.UUID
        Corresponding `stdlib` `UUID` object
    """
    return UUID(bytes=urlsafe_b64decode(s.rstrip('=') + '=='))


def uuid_to_b64id(value: UUID) -> str:
    """Convert an :class:`uuid.UUID` object to a Base64 URL safe ID string 

    Parameters
    ----------

    value : uuid.UUID
        The UUID to convert

    Returns
    -------
    str
        Base64 URL safe ID string
    """
    return B64UUID(value).string


class B64UUID:
    def __init__(self, initial: Union[None, UUID, str, bytes, int] = None):
        """Class represents Base64 URL safe UUID

        Parameters
        ----------

        initial : None, uuid.UUID, str, bytes, int
            Create the instance from the UUID initial value.

            When the parameter is:

            - :data:`None` (`default`) : initial value is automatic generated using :func:`uuid.uuid4`
            - :class:`uuid.UUID` : Create the instance by this object directly
            - :class:`str` : It should be either an a string of 32 hexadecimal digits or Base64 URL safe UUID string.
              It will be converted to :class:`uuid.UUID`
            - :class:`bytes` : 16 bytes in big-endian order as the bytes, that will be converted to :class:`uuid.UUID`
            - :class:`int` : a single 128-bit integer, that will be converted to :class:`uuid.UUID`
        """
        if initial is None:
            self._uuid = uuid4()
        elif isinstance(initial, UUID):
            self._uuid = initial
        elif isinstance(initial, str):
            if len(initial) < 32:
                self._uuid = b64id_to_uuid(initial)
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
        """`UUID` of the instance

        Returns
        -------
        uuid.UUID
            Corresponding `stdlib` `UUID` object of the instance
        """
        return self._uuid

    @property
    def string(self) -> str:
        """Base64 URL safe UUID of the instance

        Returns
        -------
        str
            An URL safe string represents the `UUID` value of the instance

        Note
        ----

        Same as data convertion to :class:`str`::

            bid = Base64UUID()
            s1 = bid.string
            s2 = str(bid)
            assert s1 == s2  # equals!
        """
        return self._string
