from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: Optional[object] = field(
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
                {
                    "name": "c1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "c3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "c4",
                    "type": object,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
