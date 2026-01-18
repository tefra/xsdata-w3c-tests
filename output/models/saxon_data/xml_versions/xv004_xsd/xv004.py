from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class A(Enum):
    B = "B𠀀"


@dataclass(kw_only=True)
class DKstra:
    class Meta:
        name = "Dĳkstra"

    a: None | A = field(
        default=None,
        metadata={
            "name": "A𰀀",
            "type": "Attribute",
        },
    )
