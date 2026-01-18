from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    r1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
            "required": True,
        }
    )
