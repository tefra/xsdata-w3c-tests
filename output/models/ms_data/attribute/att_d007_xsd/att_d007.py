from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


class Char(Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"


class No(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


@dataclass
class AttRef:
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
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
