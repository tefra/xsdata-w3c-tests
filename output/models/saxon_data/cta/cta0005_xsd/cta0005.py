from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://cta0002/"


class TMin(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


@dataclass
class T:
    class Meta:
        name = "t"

    e: list[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://cta0002/",
        },
    )
    min: Optional[TMin] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://cta0002/",
        },
    )


@dataclass
class Message(T):
    class Meta:
        name = "message"
        namespace = "http://cta0002/"


@dataclass
class Treq(T):
    class Meta:
        name = "treq"

    e: list[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://cta0002/",
            "min_occurs": 1,
        },
    )


@dataclass
class Messages:
    class Meta:
        name = "messages"
        namespace = "http://cta0002/"

    message: list[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
