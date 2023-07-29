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
                    "namespace": "http://www.w3.org/1999/xhtml",
                    "process_contents": "skip",
                },
                {
                    "name": "d",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "b",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "a",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "c",
                    "type": bool,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
