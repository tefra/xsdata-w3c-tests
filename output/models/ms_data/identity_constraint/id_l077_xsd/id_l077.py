from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Ttype:
    class Meta:
        name = "ttype"

    col: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "row",
                    "type": ForwardRef("Ttype.Row"),
                    "namespace": "myNS.tempuri.org",
                },
                {
                    "name": "ref",
                    "type": ForwardRef("Ttype.Ref"),
                    "namespace": "myNS.tempuri.org",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Row:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        x: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            },
        )

    @dataclass(kw_only=True)
    class Ref:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        y: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            },
        )


@dataclass(kw_only=True)
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
