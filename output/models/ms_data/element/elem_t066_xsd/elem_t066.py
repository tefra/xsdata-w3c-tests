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


class ListA(Enum):
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


class ListAb(Enum):
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
class Sa3:
    """
    :ivar any_element:
    """
    class Meta:
        name = "sa3"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class EA:
    """
    :ivar value:
    :ivar att:
    """
    class Meta:
        name = "E-A"

    value: Optional[A] = field(
        default=None,
    )
    att: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
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
class Sa1:
    """
    :ivar value:
    """
    class Meta:
        name = "sa1"

    value: Optional[RA] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Test1:
    """
    :ivar value:
    """
    class Meta:
        name = "test1"

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
    """
    :ivar sa3:
    :ivar sa2:
    :ivar sa1:
    :ivar test1:
    :ivar test2:
    :ivar test3:
    :ivar test4:
    :ivar test5:
    """
    class Meta:
        name = "root"

    sa3: List[Sa3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    sa2: List[Sa2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    sa1: List[Sa1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )
    test1: List[Test1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=5
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
    test5: Optional[Test5] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
