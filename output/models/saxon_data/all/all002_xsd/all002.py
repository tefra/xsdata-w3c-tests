from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class C1:
    class Meta:
        name = "C"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class D1:
    class Meta:
        name = "D"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class C2:
    class Meta:
        name = "c"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class D2:
    class Meta:
        name = "d"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    c_element: List[C1] = field(
        default_factory=list,
        metadata={
            "name": "C",
            "type": "Element",
            "min_occurs": 2,
        }
    )
    c: List[C2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        }
    )
    d_element: Optional[D1] = field(
        default=None,
        metadata={
            "name": "D",
            "type": "Element",
            "required": True,
        }
    )
    d: Optional[D2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
