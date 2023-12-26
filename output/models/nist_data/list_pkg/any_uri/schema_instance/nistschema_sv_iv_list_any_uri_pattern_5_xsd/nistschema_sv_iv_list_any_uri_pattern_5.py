from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-pattern-5-NS"


@dataclass
class NistschemaSvIvListAnyUriPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-pattern-5"
        namespace = "NISTSchema-SV-IV-list-anyURI-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,9}\.){1,3}\c{3} \c{3,6}://(\c{1,8}\.){1,3}\c{3} \c{3,6}://(\c{1,4}\.){1,3}\c{3} \c{3,6}://(\c{1,4}\.){1,4}\c{3} \c{3,6}://(\c{1,4}\.){1,4}\c{3} \c{3,6}://(\c{1,7}\.){1,5}\c{3} \c{3,6}://(\c{1,8}\.){1,5}\c{3}",
            "tokens": True,
        },
    )
