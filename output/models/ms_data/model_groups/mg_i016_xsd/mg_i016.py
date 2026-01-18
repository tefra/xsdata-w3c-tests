from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    choice: (
        None
        | Foo.G1
        | Foo.G12
        | Foo.G2
        | Foo.G22
        | Foo.G3
        | Foo.G32
        | Foo.G4
        | Foo.G42
        | Foo.C1
        | Foo.C2
        | Foo.C3
        | Foo.C4
    ) = field(
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

    @dataclass(kw_only=True)
    class G1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G12:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G22:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G32:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G4:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class G42:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C1:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C2:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C3:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )

    @dataclass(kw_only=True)
    class C4:
        content: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "",
            },
        )


@dataclass(kw_only=True)
class Doc(Foo):
    class Meta:
        name = "doc"
