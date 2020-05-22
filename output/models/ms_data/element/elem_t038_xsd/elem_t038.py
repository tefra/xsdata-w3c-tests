from enum import Enum
from dataclasses import dataclass, field
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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=2
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
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
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    y: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
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
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Test2:
    """
    :ivar any_element:
    """
    class Meta:
        name = "test2"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
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
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
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
        metadata=dict(
            required=True
        )
    )


@dataclass
class Test3(Ca):
    class Meta:
        name = "test3"


@dataclass
class Root:
    """
    :ivar s_a:
    :ivar test:
    :ivar test2:
    :ivar test3:
    """
    class Meta:
        name = "root"

    s_a: Optional[SA] = field(
        default=None,
        metadata=dict(
            name="s-a",
            type="Element"
        )
    )
    test: Optional[Test] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    test2: Optional[Test2] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    test3: Optional[Test3] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
