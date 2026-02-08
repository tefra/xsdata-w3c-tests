from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    r1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    r2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 4,
            "sequence": 1,
        },
    )
    r3: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class Elem(ComplexType):
    class Meta:
        name = "elem"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: Elem = field(
        metadata={
            "type": "Element",
        }
    )
