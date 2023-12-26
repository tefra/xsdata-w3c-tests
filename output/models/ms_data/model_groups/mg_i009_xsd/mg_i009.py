from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Foo:
    class Meta:
        name = "foo"

    choice: List[Union[int, str, bool, object]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": int,
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
                    "name": "c",
                    "type": bool,
                    "namespace": "",
                },
                {
                    "name": "d",
                    "type": object,
                    "namespace": "",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                    "process_contents": "skip",
                },
            ),
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
