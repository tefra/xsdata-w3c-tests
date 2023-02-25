from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bar:
    class Meta:
        name = "bar"

    e1_or_e2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        }
    )


@dataclass
class Foo(Bar):
    class Meta:
        name = "foo"


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
