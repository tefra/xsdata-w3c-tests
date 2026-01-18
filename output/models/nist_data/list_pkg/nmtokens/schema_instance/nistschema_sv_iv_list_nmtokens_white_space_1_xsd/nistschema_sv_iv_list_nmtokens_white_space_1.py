from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListNmtokensWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
