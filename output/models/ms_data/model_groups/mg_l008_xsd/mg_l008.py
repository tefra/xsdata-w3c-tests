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
                    "name": "e1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "e3",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "e4",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "e5",
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
