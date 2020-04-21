from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union


class A(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class B(Enum):
    """
    :cvar A:
    :cvar B:
    :cvar C123456789:
    """
    A = "a"
    B = "b"
    C123456789 = "c123456789"


class RA(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"

    value: Optional[Union[A, B]] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar test:
    """
    class Meta:
        name = "root"

    test: List[Test] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
