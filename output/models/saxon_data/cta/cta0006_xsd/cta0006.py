from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
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
        }
    )
    value: Optional[Union[Decimal, int, XmlDate, XmlTime, QName, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DateMessageType(MessageType):
    class Meta:
        name = "dateMessageType"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DecimalMessageType(MessageType):
    class Meta:
        name = "decimalMessageType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class IntMessageType(MessageType):
    class Meta:
        name = "intMessageType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass
class QNameMessageType(MessageType):
    class Meta:
        name = "qNameMessageType"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class StringMessageType(MessageType):
    class Meta:
        name = "stringMessageType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeMessageType(MessageType):
    class Meta:
        name = "timeMessageType"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Messages:
    class Meta:
        name = "messages"

    message: List[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
