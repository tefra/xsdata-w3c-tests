from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.example.org"


@dataclass
class Mod2Sequence:
    class Meta:
        name = "MOD2_SEQUENCE"

    y: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class X(Mod2Sequence):
    class Meta:
        name = "x"
        namespace = "http://www.example.org"
