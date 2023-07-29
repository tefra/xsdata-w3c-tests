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
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n1",
                    "process_contents": "skip",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n2",
                    "process_contents": "skip",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n3",
                    "process_contents": "skip",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n4",
                    "process_contents": "skip",
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
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
