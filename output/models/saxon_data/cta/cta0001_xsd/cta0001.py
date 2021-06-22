from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
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

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    kind: Optional[MessageTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class Message(MessageType):
    class Meta:
        name = "message"


@dataclass
class MessageTypeBase64(MessageType):
    class Meta:
        name = "messageTypeBase64"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "format": "base64",
        }
    )


@dataclass
class MessageTypeDate(MessageType):
    class Meta:
        name = "messageTypeDate"

    value: Optional[XmlDate] = field(
        default=None,
    )


@dataclass
class MessageTypeString(MessageType):
    class Meta:
        name = "messageTypeString"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class MessageTypeTime(MessageType):
    class Meta:
        name = "messageTypeTime"

    value: Optional[XmlTime] = field(
        default=None,
    )


@dataclass
class MessageTypeXml(MessageType):
    class Meta:
        name = "messageTypeXML"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
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
