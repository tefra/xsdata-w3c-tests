from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ϐ"
    A0 = "a0-ϓ"
    A0_A = "a0Aϖ"
    A10 = "a10Ϣ"
    A1 = "a1-ϩ"
    A1_A = "a1Aϱ"
    A20 = "a20Ё"
    A2 = "a2-І"
    A2_A = "a2AЌ"
    A30 = "a30Ў"
    A3 = "a3-Ю"
    A3_A = "a3Aя"
    A40 = "a40ё"
    A4 = "a4-і"
    A4_A = "a4Aќ"
    A50 = "a50ў"
    A5 = "a5-ѯ"
    A5_A = "a5Aҁ"
    A60 = "a60Ґ"
    A6 = "a6-ҧ"
    A6_A = "a6Aҿ"
    A70 = "a70Ӂ"
    A7 = "a7-ӂ"
    A7_A = "a7Aӄ"
    A80 = "a80Ӈ"
    A8 = "a8-Ӈ"
    A8_A = "a8Aӈ"
    A90 = "a90Ӌ"
    A9 = "a9-Ӌ"
    A9_A = "a9Aӌ"


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
