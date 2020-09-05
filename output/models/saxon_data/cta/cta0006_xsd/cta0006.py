from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xml.etree.ElementTree import QName


@dataclass
class DateMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "dateMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DecimalMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "decimalMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class IntMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "intMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class MessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "messageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[Union[Decimal, int, str, QName]] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class QNameMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "qNameMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class StringMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "stringMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class TimeMessageType:
    """
    :ivar kind:
    :ivar value:
    """
    class Meta:
        name = "timeMessageType"

    kind: Optional[QName] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Message(MessageType):
    class Meta:
        name = "message"


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
