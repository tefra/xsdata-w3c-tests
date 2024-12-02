from dataclasses import dataclass, field
from typing import ForwardRef, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    col: Optional[str] = field(
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

    @dataclass
    class Row:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        x: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            },
        )

    @dataclass
    class Ref:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        y: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            },
        )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass
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
