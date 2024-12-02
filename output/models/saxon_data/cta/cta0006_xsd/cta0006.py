from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class MessageType:
    class Meta:
        name = "messageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: Optional[Union[Decimal, int, XmlDate, XmlTime, QName, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DateMessageType(MessageType):
    class Meta:
        name = "dateMessageType"


@dataclass
class DecimalMessageType(MessageType):
    class Meta:
        name = "decimalMessageType"


@dataclass
class IntMessageType(MessageType):
    class Meta:
        name = "intMessageType"


@dataclass
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass
class QNameMessageType(MessageType):
    class Meta:
        name = "qNameMessageType"


@dataclass
class StringMessageType(MessageType):
    class Meta:
        name = "stringMessageType"


@dataclass
class TimeMessageType(MessageType):
    class Meta:
        name = "timeMessageType"


@dataclass
class Messages:
    class Meta:
        name = "messages"

    message: list[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
