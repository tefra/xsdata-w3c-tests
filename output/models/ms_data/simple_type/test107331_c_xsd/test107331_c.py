from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class A1(Enum):
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
class A2:
    """
    :ivar value:
    """
    class Meta:
        name = "A"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 0,
            "max_inclusive": 10,
        }
    )


class B1(Enum):
    """
    :cvar A:
    :cvar B:
    :cvar C123456789:
    """
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class B2:
    """
    :ivar value:
    """
    class Meta:
        name = "B"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 10,
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
class Item:
    """
    :ivar value:
    """
    class Meta:
        name = "item"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class A3:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[A1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B3:
    """
    :ivar value:
    """
    class Meta:
        name = "b"

    value: Optional[B1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class La:
    """
    :ivar value:
    """
    class Meta:
        name = "la"

    value: List[A1] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class Lab:
    """
    :ivar value:
    """
    class Meta:
        name = "lab"

    value: List[UnionAb] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class Ra:
    """
    :ivar value:
    """
    class Meta:
        name = "ra"

    value: Optional[RA] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar ra:
    :ivar lab:
    :ivar la:
    :ivar uab:
    :ivar ua:
    :ivar b_element:
    :ivar a_element:
    :ivar b:
    :ivar a:
    :ivar item:
    """
    class Meta:
        name = "root"

    ra: List[RA] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    lab: List[List[UnionAb]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    la: List[List[A1]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    uab: List[UnionAb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    ua: List[UnionA] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    b_element: List[B1] = field(
        default_factory=list,
        metadata={
            "name": "b",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    a_element: List[A1] = field(
        default_factory=list,
        metadata={
            "name": "a",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    b: List[B1] = field(
        default_factory=list,
        metadata={
            "name": "B",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    a: List[A1] = field(
        default_factory=list,
        metadata={
            "name": "A",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    item: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Ua:
    """
    :ivar value:
    """
    class Meta:
        name = "ua"

    value: Optional[UnionA] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Uab:
    """
    :ivar value:
    """
    class Meta:
        name = "uab"

    value: Optional[UnionAb] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
