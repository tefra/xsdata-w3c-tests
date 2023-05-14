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
                {
                    "name": "s1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "s2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "s3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "s4",
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
