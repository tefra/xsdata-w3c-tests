from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://cta0002/"


@dataclass
class T:
    """
    :ivar e:
    :ivar min:
    """
    class Meta:
        name = "t"

    e: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://cta0002/",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    min: Optional["T.Min"] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://cta0002/"
        )
    )

    class Min(Enum):
        """
        :cvar VALUE_0:
        :cvar VALUE_1:
        """
        VALUE_0 = 0
        VALUE_1 = 1


@dataclass
class Treq:
    """
    :ivar e:
    :ivar min:
    """
    class Meta:
        name = "treq"

    e: List[Decimal] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://cta0002/",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    min: Optional["Treq.Min"] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://cta0002/"
        )
    )

    class Min(Enum):
        """
        :cvar VALUE_0:
        :cvar VALUE_1:
        """
        VALUE_0 = 0
        VALUE_1 = 1


@dataclass
class Message(T):
    class Meta:
        name = "message"
        namespace = "http://cta0002/"



@dataclass
class Messages:
    """
    :ivar message:
    """
    class Meta:
        name = "messages"
        namespace = "http://cta0002/"

    message: List[Message] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
