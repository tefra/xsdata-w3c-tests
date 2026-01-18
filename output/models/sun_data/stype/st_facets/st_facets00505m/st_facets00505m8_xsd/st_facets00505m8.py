from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ั"
    A10 = "a10ิ"
    A1 = "a1-ื"
    A1_A = "a1Aฺ"
    A20 = "a20็"
    A2 = "a2-๊"
    A2_A = "a2A๎"
    A30 = "a30ັ"
    A40 = "a40ິ"
    A4 = "a4-ຶ"
    A4_A = "a4Aູ"
    A50 = "a50ົ"
    A5 = "a5-ົ"
    A5_A = "a5Aຼ"
    A60 = "a60່"
    A6 = "a6-໊"
    A6_A = "a6Aໍ"
    A70 = "a70༘"
    A7 = "a7-༘"
    A7_A = "a7A༙"
    A80 = "a80༵"
    A90 = "a90༷"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: list[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
