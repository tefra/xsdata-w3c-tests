from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ٱ"
    A0 = "a0-ڔ"
    A0_A = "a0Aڷ"
    A10 = "a10ں"
    A1 = "a1-ڼ"
    A1_A = "a1Aھ"
    A20 = "a20ۀ"
    A2 = "a2-ۇ"
    A2_A = "a2Aێ"
    A30 = "a30ې"
    A3 = "a3-ۑ"
    A3_A = "a3Aۓ"
    A40 = "a40ە"
    A50 = "a50ۥ"
    A5 = "a5-ۥ"
    A5_A = "a5Aۦ"
    A60 = "a60अ"
    A6 = "a6-ट"
    A6_A = "a6Aह"
    A70 = "a70ऽ"
    A80 = "a80क़"
    A8 = "a8-ड़"
    A8_A = "a8Aॡ"
    A90 = "a90অ"
    A9 = "a9-ঈ"
    A9_A = "a9Aঌ"


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
