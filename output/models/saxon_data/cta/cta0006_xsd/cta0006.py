from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDate, XmlTime


@dataclass(kw_only=True)
class MessageType:
    class Meta:
        name = "messageType"

    kind: None | QName = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    value: None | Decimal | int | XmlDate | XmlTime | QName | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DateMessageType(MessageType):
    class Meta:
        name = "dateMessageType"


@dataclass(kw_only=True)
class DecimalMessageType(MessageType):
    class Meta:
        name = "decimalMessageType"


@dataclass(kw_only=True)
class IntMessageType(MessageType):
    class Meta:
        name = "intMessageType"


@dataclass(kw_only=True)
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass(kw_only=True)
class QNameMessageType(MessageType):
    class Meta:
        name = "qNameMessageType"


@dataclass(kw_only=True)
class StringMessageType(MessageType):
    class Meta:
        name = "stringMessageType"


@dataclass(kw_only=True)
class TimeMessageType(MessageType):
    class Meta:
        name = "timeMessageType"


@dataclass(kw_only=True)
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
