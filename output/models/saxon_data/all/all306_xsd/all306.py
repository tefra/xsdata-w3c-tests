from dataclasses import dataclass, field
from typing import List


@dataclass
class B:
    class Meta:
        name = "b"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Ext(B):
    class Meta:
        name = "ext"


@dataclass
class Doc(Ext):
    class Meta:
        name = "doc"
