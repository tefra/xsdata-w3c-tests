from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-d"


@dataclass
class CtA:
    class Meta:
        name = "ct-A"

    a1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    a2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "ns-d"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-d"
