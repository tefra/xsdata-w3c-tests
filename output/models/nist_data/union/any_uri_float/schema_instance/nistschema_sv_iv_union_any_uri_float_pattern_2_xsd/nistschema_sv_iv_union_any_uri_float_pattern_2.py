from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-2"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\c{3,6}://(\c{1,11}\.){1,4}\c{3}",
        },
    )
