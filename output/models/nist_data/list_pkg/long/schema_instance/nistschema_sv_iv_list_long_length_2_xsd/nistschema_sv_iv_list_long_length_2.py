from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-length-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListLongLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-long-length-2"
        namespace = "NISTSchema-SV-IV-list-long-length-2-NS"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
