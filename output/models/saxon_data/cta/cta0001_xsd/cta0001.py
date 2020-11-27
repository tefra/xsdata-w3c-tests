from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


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
    kind: Optional["MessageType.Value"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )

    class Value(Enum):
        STRING = "string"
        BASE64 = "base64"
        BINARY = "binary"
        DATE = "date"
        TIME = "time"
        XML = "xml"
        XML_1 = "XML"


@dataclass
class MessageTypeXml:
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
    kind: Optional["MessageTypeXml.Value"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )

    class Value(Enum):
        STRING = "string"
        BASE64 = "base64"
        BINARY = "binary"
        DATE = "date"
        TIME = "time"
        XML = "xml"
        XML_1 = "XML"


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
