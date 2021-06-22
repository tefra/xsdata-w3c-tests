from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##any",
                },
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
            ),
            "min_occurs": 5,
            "max_occurs": 8,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
