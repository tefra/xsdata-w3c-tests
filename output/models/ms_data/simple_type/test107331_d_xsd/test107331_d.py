from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class C:
    """
    :ivar value:
    """
    class Meta:
        name = "c"

    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class D:
    """
    :ivar value:
    """
    class Meta:
        name = "d"

    value: List[Union[Decimal, int, bool]] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )


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
class Root:
    """
    :ivar d:
    :ivar c:
    :ivar b:
    :ivar a:
    :ivar item:
    """
    class Meta:
        name = "root"

    d: List[List[Union[Decimal, int, bool]]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    c: List[List[Decimal]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    b: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    a: List[object] = field(
        default_factory=list,
        metadata={
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
