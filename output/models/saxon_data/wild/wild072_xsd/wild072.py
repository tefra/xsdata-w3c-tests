from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A1:
    class Meta:
        name = "A"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class A2:
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    a_element: Optional[A1] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
