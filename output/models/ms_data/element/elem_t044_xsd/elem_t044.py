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


@dataclass
class Sa:
    """
    :ivar any_element:
    """
    class Meta:
        name = "sa"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Test4:
    """
    :ivar any_element:
    """
    class Meta:
        name = "test4"

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
class Test2:
    """
    :ivar value:
    """
    class Meta:
        name = "test2"

    value: Optional[A] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Test3:
    """
    :ivar value:
    """
    class Meta:
        name = "test3"

    value: Optional[A] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar sa:
    :ivar test:
    :ivar test2:
    :ivar test3:
    :ivar test4:
    """
    class Meta:
        name = "root"

    sa: Optional[Sa] = field(
        default=None,
        metadata=dict(
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
    test4: Optional[Test4] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )