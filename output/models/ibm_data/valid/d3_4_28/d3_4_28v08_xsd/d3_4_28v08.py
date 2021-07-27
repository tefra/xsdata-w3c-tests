from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v08"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v08"

    el_max_inclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "2000-02-01T02:00:00+09:00",
            "max_inclusive": "2002-02-01T00:00:00+09:00",
            "pattern": r"[1-2][0][0][0-9][-][0-1][1-2][-][0-3][1-8][T]*.*",
        }
    )
    el_max_inclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": "2000-02-01T00:00:00+09:00",
            "max_inclusive": "2002-02-01T00:00:00+09:00",
            "pattern": r"[1-2][0][0][0-9][-][0-1][1-2][-][0-3][1-8][T]*.*",
        }
    )
    el_max_inclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_inclusive": "2002-01-01T00:00:00+09:00",
            "pattern": r"[1-2][0][0][0-9][-][0-1][1-2][-][0-3][1-8][T]*.*",
        }
    )
    el_max_inclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": "2002-01-31T23:59:59+09:00",
            "max_inclusive": "2002-02-01T00:00:00+09:00",
            "pattern": r"[1-2][0][0][0-9][-][0-1][1-2][-][0-3][1-8][T]*.*",
        }
    )
