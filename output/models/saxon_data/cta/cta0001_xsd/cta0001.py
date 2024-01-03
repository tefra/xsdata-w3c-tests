from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Any
from xsdata.models.datatype import XmlDate, XmlTime


class MessageTypeValue(Enum):
    STRING = "string"
    BASE64 = "base64"
    BINARY = "binary"
    DATE = "date"
    TIME = "time"
    XML = "xml"
    XML_1 = "XML"


@dataclass
class MessageType:
    class Meta:
        name = "messageType"

    kind: Optional[MessageTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass
class MessageTypeBase64(MessageType):
    class Meta:
        name = "messageTypeBase64"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[bytes] = field(
        default=None,
        metadata={
            "format": "base64",
        },
    )


@dataclass
class MessageTypeDate(MessageType):
    class Meta:
        name = "messageTypeDate"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[XmlDate] = field(default=None)


@dataclass
class MessageTypeString(MessageType):
    class Meta:
        name = "messageTypeString"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")


@dataclass
class MessageTypeTime(MessageType):
    class Meta:
        name = "messageTypeTime"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[XmlTime] = field(default=None)


@dataclass
class MessageTypeXml(MessageType):
    class Meta:
        name = "messageTypeXML"

    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
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
        },
    )
