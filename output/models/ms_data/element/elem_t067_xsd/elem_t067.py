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


@dataclass
class RCa:
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
    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


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
class Sa3:
    class Meta:
        name = "sa3"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class EA:
    class Meta:
        name = "E-A"

    value: Optional[A] = field(
        default=None,
    )
    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class Sa1:
    class Meta:
        name = "sa1"

    value: Optional[RA] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test1:
    class Meta:
        name = "test1"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test2:
    class Meta:
        name = "test2"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test3:
    class Meta:
        name = "test3"

    value: Optional[A] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Test4(Ca):
    class Meta:
        name = "test4"


@dataclass
class Test5(Ca):
    class Meta:
        name = "test5"


@dataclass
class Sa2(EA):
    class Meta:
        name = "sa2"


@dataclass
class Root:
    class Meta:
        name = "root"

    sa3: List[Sa3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    sa2: List[Sa2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    sa1: List[RA] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    test1: List[A] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    test2: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    test3: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    test4: Optional[Test4] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    test5: Optional[Test5] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
