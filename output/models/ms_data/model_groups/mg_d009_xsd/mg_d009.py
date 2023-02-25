from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    class Meta:
        name = "test"

    a_or_b: Optional[object] = field(
        default=None,
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
        }
    )


@dataclass
class Root(Test):
    class Meta:
        name = "root"
