from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-pattern-2-NS"


@dataclass
class NistschemaSvIvListAnyUriPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-pattern-2"
        namespace = "NISTSchema-SV-IV-list-anyURI-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,10}\.){1,5}\c{3} \c{3,6}://(\c{1,4}\.){1,2}\c{3} \c{3,6}://(\c{1,6}\.){1,3}\c{3} \c{3,6}://(\c{1,4}\.){1,3}\c{3} \c{3,6}://(\c{1,5}\.){1,4}\c{3} \c{3,6}://(\c{1,6}\.){1,5}\c{3} \c{3,6}://(\c{1,3}\.){1,2}\c{3} \c{3,6}://(\c{1,8}\.){1,5}\c{3}",
            "tokens": True,
        }
    )
