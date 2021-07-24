from dataclasses import dataclass, field
from typing import List


@dataclass
class B:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
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
                {
                    "name": "c",
                    "type": object,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class R(B):
    pass


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
