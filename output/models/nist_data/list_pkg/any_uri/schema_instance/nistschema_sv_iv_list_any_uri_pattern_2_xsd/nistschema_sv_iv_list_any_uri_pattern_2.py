from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListAnyUriPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-pattern-2"
        namespace = "NISTSchema-SV-IV-list-anyURI-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,10}\.){1,5}\c{3} \c{3,6}://(\c{1,4}\.){1,2}\c{3} \c{3,6}://(\c{1,6}\.){1,3}\c{3} \c{3,6}://(\c{1,4}\.){1,3}\c{3} \c{3,6}://(\c{1,5}\.){1,4}\c{3} \c{3,6}://(\c{1,6}\.){1,5}\c{3} \c{3,6}://(\c{1,3}\.){1,2}\c{3} \c{3,6}://(\c{1,8}\.){1,5}\c{3}",
            "tokens": True,
        },
    )
