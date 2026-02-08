from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Restrict(Enum):
    ADS = "ads"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    a: Restrict = field(
        init=False,
        default=Restrict.ADS,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
