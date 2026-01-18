from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDoubleLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-length-2"
        namespace = "NISTSchema-SV-IV-list-double-length-2-NS"

    value: list[float] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
