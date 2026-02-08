from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://simple001.ly/"


@dataclass(kw_only=True)
class Chap:
    class Meta:
        name = "chap"

    section: list[Chap.Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://simple001.ly/",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Section:
        value: str = field(default="")
        nr: float = field(
            default=float("inf"),
            metadata={
                "type": "Attribute",
            },
        )
        ref: float = field(
            init=False,
            default=float("inf"),
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://simple001.ly/"

    chap_or_appx: list[Doc.Chap | Doc.Appx] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "chap",
                    "type": ForwardRef("Doc.Chap"),
                },
                {
                    "name": "appx",
                    "type": ForwardRef("Doc.Appx"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Chap(Chap):
        pass

    @dataclass(kw_only=True)
    class Appx(Chap):
        pass
