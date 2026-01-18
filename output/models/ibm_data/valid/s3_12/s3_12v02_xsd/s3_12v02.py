from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "http://xstest-tns"


@dataclass(kw_only=True)
class TitleType:
    class Meta:
        name = "titleType"

    type_value: None | object = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class MixedTitleType(TitleType):
    class Meta:
        name = "mixedTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: int | str = field(default="")


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: list[
        TitleType | MixedTitleType | Root.TypeText | Root.TypeNumber
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )

    @dataclass(kw_only=True)
    class TypeText(TitleType):
        content: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        value: str = field(default="")

    @dataclass(kw_only=True)
    class TypeNumber(TitleType):
        content: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        value: int = field()
