from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    choice: list[
        Union[
            "Nametest.Ele",
            "Nametest.LowLineHyphenMinus",
            "Nametest.LowLineFullStop",
            "Nametest.Type9",
            "Nametest.LowLineLowLineLowLine",
            "Nametest.AA",
            "Nametest.AAA",
            "Nametest.AEle",
        ]
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

    @dataclass
    class Ele:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class LowLineHyphenMinus:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class LowLineFullStop:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Type9:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class LowLineLowLineLowLine:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AA:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AAA:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class AEle:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
