from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-5"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{1}E\-\d{2}",
        },
    )
