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
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n1",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n2",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n3",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://n4",
                },
            ),
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
