from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class A:
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
    class Meta:
        name = "b"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class C:
    class Meta:
        name = "c"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class D:
    class Meta:
        name = "d"

    value: List[Union[float, int, bool]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Item:
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
    class Meta:
        name = "root"

    d: List[List[Union[float, int, bool]]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    c: List[List[float]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "tokens": True,
        }
    )
    b: List[float] = field(
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
