from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class T1:
    class Meta:
        name = "t1"

    a1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    a2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class T0:
    class Meta:
        name = "t0"

    e1: List[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    e2: List[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    e3: List[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class RootType:
    class Meta:
        name = "rootType"

    hi1: Optional[T0] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    hi2: Optional[T0] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "a"
