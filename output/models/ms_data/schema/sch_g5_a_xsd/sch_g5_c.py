from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-b"


@dataclass(kw_only=True)
class CtC:
    class Meta:
        name = "ct-C"

    a1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    a2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "ns-b"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-b"
