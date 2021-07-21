from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[object] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[object] = field(
        default=None
    )


@dataclass
class Ct3:
    class Meta:
        name = "ct3"

    elem: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Ct4State(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(
        default=None
    )


@dataclass
class Ct4:
    class Meta:
        name = "ct4"

    value: Optional[str] = field(
        default=None
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    state: Optional[Ct4State] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class C(Ct4):
    class Meta:
        name = "c"


@dataclass
class Root:
    class Meta:
        name = "root"

    c: List[C] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
