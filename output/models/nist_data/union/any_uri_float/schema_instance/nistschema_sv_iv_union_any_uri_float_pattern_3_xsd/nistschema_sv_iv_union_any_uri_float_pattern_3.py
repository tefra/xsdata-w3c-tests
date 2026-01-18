from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionAnyUriFloatPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-3"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,4}\.){1,4}\c{3}",
        },
    )
