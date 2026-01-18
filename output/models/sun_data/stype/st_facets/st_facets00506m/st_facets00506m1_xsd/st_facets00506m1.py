from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A00 = "a00·"
    A10 = "a10ː"
    A20 = "a20ˑ"
    A30 = "a30·"
    A40 = "a40ـ"
    A50 = "a50ๆ"
    A60 = "a60ໆ"
    A70 = "a70々"
    A80 = "a80〱"
    A8 = "a8-〳"
    A8_A = "a8A〵"
    A90 = "a90ゝ"
    A9 = "a9-ゝ"
    A9_A = "a9Aゞ"


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
