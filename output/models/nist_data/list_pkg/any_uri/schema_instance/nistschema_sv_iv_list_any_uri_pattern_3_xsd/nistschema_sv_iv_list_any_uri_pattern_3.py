from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListAnyUriPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-pattern-3"
        namespace = "NISTSchema-SV-IV-list-anyURI-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,9}\.){1,3}\c{3} \c{3,6}://(\c{1,7}\.){1,4}\c{3} \c{3,6}://(\c{1,7}\.){1,5}\c{3} \c{3,6}://(\c{1,7}\.){1,4}\c{3} \c{3,6}://(\c{1,10}\.){1,4}\c{3} \c{3,6}://(\c{1,10}\.){1,5}\c{3} \c{3,6}://(\c{1,10}\.){1,4}\c{3} \c{3,6}://(\c{1,5}\.){1,2}\c{3}",
            "tokens": True,
        },
    )
