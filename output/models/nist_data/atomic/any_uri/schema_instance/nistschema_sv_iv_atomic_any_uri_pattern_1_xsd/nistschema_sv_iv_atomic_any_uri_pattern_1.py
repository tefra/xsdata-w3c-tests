from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\c{3,6}://(\c{1,7}\.){1,2}\c{3}",
        },
    )
