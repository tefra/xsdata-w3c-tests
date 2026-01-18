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
class IntegerTitleType(TitleType):
    class Meta:
        name = "integerTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: int = field()


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
class StringTitleType(TitleType):
    class Meta:
        name = "stringTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: list[
        TitleType | StringTitleType | IntegerTitleType | MixedTitleType
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
