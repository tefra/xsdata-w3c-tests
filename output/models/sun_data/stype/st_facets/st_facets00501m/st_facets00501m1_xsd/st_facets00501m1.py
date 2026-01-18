from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00_A = "a00A"
    A0_M = "a0-M"
    A0_AZ = "a0AZ"
    A10A = "a10a"
    A1_D = "a1-d"
    A1_AH = "a1Ah"
    A20J = "a20j"
    A2_R = "a2-r"
    A2_AZ = "a2Az"
    A30 = "a30À"
    A3 = "a3-Ë"
    A3_A = "a3AÖ"
    A40 = "a40Ø"
    A4 = "a4-Û"
    A4_A = "a4AÞ"
    A50 = "a50à"
    A5 = "a5-ë"
    A5_A = "a5Aö"
    A60 = "a60ø"
    A6 = "a6-û"
    A6_A = "a6Aÿ"
    A70 = "a70Ā"
    A7 = "a7-Ę"
    A7_A = "a7Aı"
    A80 = "a80Ĵ"
    A8 = "a8-Ĺ"
    A8_A = "a8Aľ"
    A90 = "a90Ł"
    A9 = "a9-ń"
    A9_A = "a9Aň"


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
