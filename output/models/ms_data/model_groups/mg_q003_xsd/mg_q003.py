from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    """
    :ivar e1_or_e2:
    """
    class Meta:
        name = "foo"

    e1_or_e2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "e2",
                    "type": str,
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
