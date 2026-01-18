from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class AppendixContent:
    class Meta:
        name = "appendixContent"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChapContent:
    class Meta:
        name = "chapContent"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Content:
    class Meta:
        name = "content"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Back:
    class Meta:
        name = "back"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Body:
    class Meta:
        name = "body"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    body: Body = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    back: Back = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
