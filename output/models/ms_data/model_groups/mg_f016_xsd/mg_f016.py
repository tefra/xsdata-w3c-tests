from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    g1_or_g12: None | Foo.G1 | Foo.G12 = field(
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
    g2_or_g22: None | Foo.G2 | Foo.G22 = field(
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
    g3_or_g32: None | Foo.G3 | Foo.G32 = field(
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
    g4_or_g42: None | Foo.G4 | Foo.G42 = field(
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
    c1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c4: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class Doc(Foo):
    class Meta:
        name = "doc"
