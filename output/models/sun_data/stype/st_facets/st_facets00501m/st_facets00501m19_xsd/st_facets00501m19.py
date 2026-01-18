from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00Ạ"
    A0 = "a0-Ọ"
    A0_A = "a0Aỹ"
    A10 = "a10ἀ"
    A1 = "a1-Ἂ"
    A1_A = "a1Aἕ"
    A20 = "a20Ἐ"
    A2 = "a2-Ἒ"
    A2_A = "a2AἝ"
    A30 = "a30ἠ"
    A3 = "a3-ἲ"
    A3_A = "a3Aὅ"
    A40 = "a40Ὀ"
    A4 = "a4-Ὂ"
    A4_A = "a4AὍ"
    A50 = "a50ὑ"
    A60 = "a60ὓ"
    A70 = "a70ὕ"
    A80 = "a80ὗ"
    A90 = "a90Ὑ"


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
