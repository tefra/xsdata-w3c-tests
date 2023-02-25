from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    c1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
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
            ),
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
