from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    VALUE_00 = "一00"
    VALUE_0 = "盒-0"
    A0 = "龥a0"
    VALUE_01 = "〇01"
    VALUE_02 = "〡02"
    VALUE_2 = "〥-2"
    A2 = "〩a2"


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
