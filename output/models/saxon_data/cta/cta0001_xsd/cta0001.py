from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from xsdata.models.datatype import XmlDate, XmlTime


class MessageTypeValue(Enum):
    STRING = "string"
    BASE64 = "base64"
    BINARY = "binary"
    DATE = "date"
    TIME = "time"
    XML = "xml"
    XML_1 = "XML"


@dataclass(kw_only=True)
class MessageType:
    class Meta:
        name = "messageType"

    kind: None | MessageTypeValue = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass(kw_only=True)
class MessageTypeBase64(MessageType):
    class Meta:
        name = "messageTypeBase64"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: bytes = field(
        default=b"",
        metadata={
            "format": "base64",
        },
    )


@dataclass(kw_only=True)
class MessageTypeDate(MessageType):
    class Meta:
        name = "messageTypeDate"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: XmlDate = field()


@dataclass(kw_only=True)
class MessageTypeString(MessageType):
    class Meta:
        name = "messageTypeString"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")


@dataclass(kw_only=True)
class MessageTypeTime(MessageType):
    class Meta:
        name = "messageTypeTime"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: XmlTime = field()


@dataclass(kw_only=True)
class MessageTypeXml(MessageType):
    class Meta:
        name = "messageTypeXML"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


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
