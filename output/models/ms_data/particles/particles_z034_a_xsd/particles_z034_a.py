from dataclasses import dataclass, field
from typing import List


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    a_or_b: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": object,
                    "namespace": "",
                },
            ),
            "min_occurs": 2,
        },
    )


@dataclass
class Doc(FooType):
    class Meta:
        name = "doc"
