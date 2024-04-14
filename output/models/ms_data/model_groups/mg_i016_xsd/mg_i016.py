from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[
        Union[
            "Foo.G1",
            "Foo.G12",
            "Foo.G2",
            "Foo.G22",
            "Foo.G3",
            "Foo.G32",
            "Foo.G4",
            "Foo.G42",
            "Foo.C1",
            "Foo.C2",
            "Foo.C3",
            "Foo.C4",
        ]
    ] = field(
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
                {
                    "name": "c1",
                    "type": ForwardRef("Foo.C1"),
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": ForwardRef("Foo.C2"),
                    "namespace": "",
                },
                {
                    "name": "c3",
                    "type": ForwardRef("Foo.C3"),
                    "namespace": "",
                },
                {
                    "name": "c4",
                    "type": ForwardRef("Foo.C4"),
                    "namespace": "",
                },
            ),
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
    class C1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C3:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class C4:
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
