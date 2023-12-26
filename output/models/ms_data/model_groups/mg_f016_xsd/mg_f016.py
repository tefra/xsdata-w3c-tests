from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    g1_or_g12: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "g12",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
    g2_or_g22: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "g22",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
    g3_or_g32: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "g32",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
    g4_or_g42: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g4",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "g42",
                    "type": object,
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
class Doc(Foo):
    class Meta:
        name = "doc"
