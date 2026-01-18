from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v06"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v06"

    el_min_inclusive_min_inclusive: list[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "2003-02-02T02:00:00+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
    el_min_inclusive_min_exclusive: list[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": "2003-02-02T02:00:00+09:00",
            "min_inclusive": "2002-02-02T02:00:00+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
    el_min_inclusive_max_inclusive: list[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "2002-02-02T02:00:00+09:00",
            "max_inclusive": "2009-02-02T02:00:00+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
    el_min_inclusive_max_exclusive: list[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "2002-02-02T02:00:00+09:00",
            "max_exclusive": "2009-02-02T02:00:00+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
