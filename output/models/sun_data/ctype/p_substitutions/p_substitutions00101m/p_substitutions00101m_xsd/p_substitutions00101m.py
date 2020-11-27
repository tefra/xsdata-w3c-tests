from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "pSubstitutions"


@dataclass
class A:
    c: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class C:
    c: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )


@dataclass
class B(A):
    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class E(A):
    class Meta:
        name = "e"
        namespace = "pSubstitutions"
