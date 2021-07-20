from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v07"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v07"

    el_min_exclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinExclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_exclusive": "2002-02-02T02:00:00+09:00",
            "min_inclusive": "2002-02-02T02:00:01+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        }
    )
    el_min_exclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinExclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_exclusive": "2002-02-02T02:00:01+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        }
    )
    el_min_exclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinExclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_exclusive": "2002-02-02T02:00:00+09:00",
            "max_inclusive": "2005-02-02T02:00:00+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        }
    )
    el_min_exclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMinExclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_exclusive": "2002-02-02T02:00:00+09:00",
            "max_exclusive": "2005-02-02T01:59:59+09:00",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        }
    )
