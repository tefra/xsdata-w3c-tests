from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ɶ"
    A0 = "a0-ɺ"
    A0_A = "a0Aɿ"
    A10 = "a10ʁ"
    A1 = "a1-ʔ"
    A1_A = "a1Aʨ"
    A20 = "a20ʻ"
    A2 = "a2-ʾ"
    A2_A = "a2Aˁ"
    A30 = "a30Ά"
    A40 = "a40Έ"
    A4 = "a4-Ή"
    A4_A = "a4AΊ"
    A50 = "a50Ό"
    A60 = "a60Ύ"
    A6 = "a6-Ύ"
    A6_A = "a6AΏ"
    A70 = "a70Α"
    A7 = "a7-Ι"
    A7_A = "a7AΡ"
    A80 = "a80Σ"
    A8 = "a8-Ω"
    A8_A = "a8Aί"
    A90 = "a90α"
    A9 = "a9-ο"
    A9_A = "a9Aώ"


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
