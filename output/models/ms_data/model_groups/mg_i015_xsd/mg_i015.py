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
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
