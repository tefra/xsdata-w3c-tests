from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


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


@dataclass
class Ca:
    """
    :ivar x:
    :ivar y:
    """
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
class RCa:
    """
    :ivar x:
    :ivar y:
    """
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


class UnionAb(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar A:
    :cvar B:
    :cvar C123456789:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class SA:
    """
    :ivar any_element:
    """
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
    """
    :ivar z:
    """
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
class Test:
    """
    :ivar value:
    """
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
    """
    :ivar s_a:
    :ivar test:
    :ivar test2:
    """
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
