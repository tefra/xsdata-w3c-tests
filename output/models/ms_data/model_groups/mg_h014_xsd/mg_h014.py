from dataclasses import dataclass, field
from typing import Optional, Any


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

    e1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        }
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
