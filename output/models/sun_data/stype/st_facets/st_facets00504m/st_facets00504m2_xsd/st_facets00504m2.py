from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00೦"
    A0 = "a0-೪"
    A0_A = "a0A೯"
    A10 = "a10൦"
    A1 = "a1-൪"
    A1_A = "a1A൯"
    A20 = "a20๐"
    A2 = "a2-๔"
    A2_A = "a2A๙"
    A30 = "a30໐"
    A3 = "a3-໔"
    A3_A = "a3A໙"
    A40 = "a40༠"
    A4 = "a4-༤"
    A4_A = "a4A༩"


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
