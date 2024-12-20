from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class ACt:
    class Meta:
        name = "A-ct"

    att1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: object = field(
        default="bar",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class E2:
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 2,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
