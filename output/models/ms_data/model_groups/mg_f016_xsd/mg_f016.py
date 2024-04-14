from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    g1_or_g12: Optional[Union["Foo.G1", "Foo.G12"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": ForwardRef("Foo.G1"),
                    "namespace": "",
                },
                {
                    "name": "g12",
                    "type": ForwardRef("Foo.G12"),
                    "namespace": "",
                },
            ),
        },
    )
    g2_or_g22: Optional[Union["Foo.G2", "Foo.G22"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g2",
                    "type": ForwardRef("Foo.G2"),
                    "namespace": "",
                },
                {
                    "name": "g22",
                    "type": ForwardRef("Foo.G22"),
                    "namespace": "",
                },
            ),
        },
    )
    g3_or_g32: Optional[Union["Foo.G3", "Foo.G32"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g3",
                    "type": ForwardRef("Foo.G3"),
                    "namespace": "",
                },
                {
                    "name": "g32",
                    "type": ForwardRef("Foo.G32"),
                    "namespace": "",
                },
            ),
        },
    )
    g4_or_g42: Optional[Union["Foo.G4", "Foo.G42"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g4",
                    "type": ForwardRef("Foo.G4"),
                    "namespace": "",
                },
                {
                    "name": "g42",
                    "type": ForwardRef("Foo.G42"),
                    "namespace": "",
                },
            ),
        },
    )
    c1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class G1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G12:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G22:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G32:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G4:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class G42:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
