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
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
