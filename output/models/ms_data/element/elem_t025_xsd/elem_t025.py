from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class B(Enum):
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class Ca:
    class Meta:
        name = "CA"

    x: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        }
    )
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class RA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class UnionA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class UnionAb(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class SA:
    class Meta:
        name = "s-a"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class ECa(Ca):
    class Meta:
        name = "E-CA"

    z: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class RCa(Ca):
    class Meta:
        name = "R-CA"

    x: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test2(Ca):
    class Meta:
        name = "test2"


@dataclass
class Root:
    class Meta:
        name = "root"

    s_a: Optional[SA] = field(
        default=None,
        metadata={
            "name": "s-a",
            "type": "Element",
        }
    )
    test: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    test2: Optional[Test2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
