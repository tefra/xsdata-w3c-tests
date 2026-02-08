from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ST_facets"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: float = field(
        metadata={
            "max_exclusive": 11.0,
        }
    )
