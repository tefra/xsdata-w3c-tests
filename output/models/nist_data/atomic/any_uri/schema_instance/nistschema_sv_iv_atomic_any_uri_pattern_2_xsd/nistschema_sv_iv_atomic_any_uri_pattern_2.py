from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,3}\.){1,4}\c{3}",
        },
    )
