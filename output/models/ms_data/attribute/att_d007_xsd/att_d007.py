from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


class Char(Enum):
    """
    :cvar A:
    :cvar B:
    :cvar C:
    :cvar D:
    :cvar E:
    """
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"


class No(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


@dataclass
class AttRef:
    """
    :ivar att1:
    """
    class Meta:
        name = "attRef"

    att1: List[Union[No, Char, int]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
            "tokens": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
