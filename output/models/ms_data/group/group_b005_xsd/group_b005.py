from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    r1_or_r2: list[ComplexType.R1 | ComplexType.R2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "r1",
                    "type": ForwardRef("ComplexType.R1"),
                    "namespace": "",
                    "max_occurs": 2,
                },
                {
                    "name": "r2",
                    "type": ForwardRef("ComplexType.R2"),
                    "namespace": "",
                    "max_occurs": 100,
                },
            ),
            "max_occurs": 100,
        },
    )

    @dataclass(kw_only=True)
    class R1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class R2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
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
