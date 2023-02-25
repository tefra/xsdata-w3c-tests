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
                    "name": "one",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "two",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "three",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "four",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "five",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "five2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "six",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "six2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "seven",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "seven2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "eight",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "eight2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
