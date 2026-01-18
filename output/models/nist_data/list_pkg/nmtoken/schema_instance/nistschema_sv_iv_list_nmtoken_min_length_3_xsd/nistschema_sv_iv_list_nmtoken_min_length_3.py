from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNmtokenMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
