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
                    "required": True,
                },
                {
                    "name": "e2",
                    "type": object,
                    "namespace": "",
                    "required": True,
                },
                {
                    "name": "e3",
                    "type": object,
                    "namespace": "",
                    "required": True,
                },
                {
                    "name": "e4",
                    "type": object,
                    "namespace": "",
                    "required": True,
                },
            ),
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
