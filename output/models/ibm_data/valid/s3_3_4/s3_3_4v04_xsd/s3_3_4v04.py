from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Entities(Enum):
    ASD_QWE = "asd qwe"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e1: Entities = field(
        default=Entities.ASD_QWE,
        metadata={
            "type": "Attribute",
        },
    )
