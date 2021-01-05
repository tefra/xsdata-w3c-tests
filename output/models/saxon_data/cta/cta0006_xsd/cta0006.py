from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xml.etree.ElementTree import QName
from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class DateMessageType:
    class Meta:
        name = "dateMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DecimalMessageType:
    class Meta:
        name = "decimalMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class IntMessageType:
    class Meta:
        name = "intMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


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
class QNameMessageType:
    class Meta:
        name = "qNameMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class StringMessageType:
    class Meta:
        name = "stringMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeMessageType:
    class Meta:
        name = "timeMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[XmlTime] = field(
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
