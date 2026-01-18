from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00ງ"
    A0 = "a0-ງ"
    A0_A = "a0Aຈ"
    A10 = "a10ຊ"
    A20 = "a20ຍ"
    A30 = "a30ດ"
    A3 = "a3-ຕ"
    A3_A = "a3Aທ"
    A40 = "a40ນ"
    A4 = "a4-ຜ"
    A4_A = "a4Aຟ"
    A50 = "a50ມ"
    A5 = "a5-ຢ"
    A5_A = "a5Aຣ"
    A60 = "a60ລ"
    A70 = "a70ວ"
    A80 = "a80ສ"
    A8 = "a8-ສ"
    A8_A = "a8Aຫ"
    A90 = "a90ອ"
    A9 = "a9-ອ"
    A9_A = "a9Aຮ"


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
