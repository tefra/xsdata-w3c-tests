from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_or_sg: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "sg",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
