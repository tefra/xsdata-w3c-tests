from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class MessageType:
    """
    :ivar any_element:
    :ivar kind:
    :ivar any_attributes:
    """
    class Meta:
        name = "messageType"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    kind: Optional["MessageType.Value"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )

    class Value(Enum):
        """
        :cvar STRING:
        :cvar BASE64:
        :cvar BINARY:
        :cvar DATE:
        :cvar TIME:
        :cvar XML:
        :cvar XML_1:
        """
        STRING = "string"
        BASE64 = "base64"
        BINARY = "binary"
        DATE = "date"
        TIME = "time"
        XML = "xml"
        XML_1 = "XML"


@dataclass
class MessageTypeXml:
    """
    :ivar any_element:
    :ivar kind:
    :ivar any_attributes:
    """
    class Meta:
        name = "messageTypeXML"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    kind: Optional["MessageTypeXml.Value"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )

    class Value(Enum):
        """
        :cvar STRING:
        :cvar BASE64:
        :cvar BINARY:
        :cvar DATE:
        :cvar TIME:
        :cvar XML:
        :cvar XML_1:
        """
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
class MessageTypeBase64(MessageType):
    """
    :ivar value:
    """
    class Meta:
        name = "messageTypeBase64"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class MessageTypeDate(MessageType):
    """
    :ivar value:
    """
    class Meta:
        name = "messageTypeDate"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class MessageTypeString(MessageType):
    """
    :ivar value:
    """
    class Meta:
        name = "messageTypeString"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class MessageTypeTime(MessageType):
    """
    :ivar value:
    """
    class Meta:
        name = "messageTypeTime"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Messages:
    """
    :ivar message:
    """
    class Meta:
        name = "messages"

    message: List[Message] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
