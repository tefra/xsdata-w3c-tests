from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Nametest:
    choice: list[
        Nametest.Ele
        | Nametest.LowLineHyphenMinus
        | Nametest.LowLineFullStop
        | Nametest.Type9
        | Nametest.LowLineLowLineLowLine
        | Nametest.AA
        | Nametest.AAA
        | Nametest.AEle
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "_ele",
                    "type": ForwardRef("Nametest.Ele"),
                    "namespace": "a",
                },
                {
                    "name": "_-",
                    "type": ForwardRef("Nametest.LowLineHyphenMinus"),
                    "namespace": "a",
                },
                {
                    "name": "_.",
                    "type": ForwardRef("Nametest.LowLineFullStop"),
                    "namespace": "a",
                },
                {
                    "name": "_9",
                    "type": ForwardRef("Nametest.Type9"),
                    "namespace": "a",
                },
                {
                    "name": "___",
                    "type": ForwardRef("Nametest.LowLineLowLineLowLine"),
                    "namespace": "a",
                },
                {
                    "name": "a_a",
                    "type": ForwardRef("Nametest.AA"),
                    "namespace": "a",
                },
                {
                    "name": "a.a",
                    "type": ForwardRef("Nametest.AAA"),
                    "namespace": "a",
                },
                {
                    "name": "ele",
                    "type": ForwardRef("Nametest.AEle"),
                    "namespace": "a",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Ele:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class LowLineHyphenMinus:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class LowLineFullStop:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class Type9:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class LowLineLowLineLowLine:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class AA:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class AAA:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class AEle:
        value: str = field(default="")


@dataclass(kw_only=True)
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
