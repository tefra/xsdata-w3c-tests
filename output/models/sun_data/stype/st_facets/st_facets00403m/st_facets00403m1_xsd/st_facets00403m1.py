from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "SType/ST_facets"


class S(StrEnum):
    VALUE_00 = "_00"


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
