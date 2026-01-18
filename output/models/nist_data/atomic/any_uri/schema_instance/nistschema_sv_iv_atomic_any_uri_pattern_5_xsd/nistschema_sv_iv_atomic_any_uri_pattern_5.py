from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,10}\.){1,5}\c{3}",
        },
    )
