from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_6_v01"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_6_v01"

    value: float = field(
        metadata={
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 5.0,
        }
    )
