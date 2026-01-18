from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class ACt:
    class Meta:
        name = "A-ct"

    att1: None | object = field(
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


@dataclass(kw_only=True)
class E2:
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 2,
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
