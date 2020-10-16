from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-pattern-1-NS"


@dataclass
class NistschemaSvIvListAnyUriPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-pattern-1"
        namespace = "NISTSchema-SV-IV-list-anyURI-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,7}\.){1,4}\c{3} \c{3,6}://(\c{1,7}\.){1,3}\c{3} \c{3,6}://(\c{1,9}\.){1,2}\c{3} \c{3,6}://(\c{1,8}\.){1,3}\c{3} \c{3,6}://(\c{1,6}\.){1,2}\c{3} \c{3,6}://(\c{1,8}\.){1,2}\c{3} \c{3,6}://(\c{1,7}\.){1,5}\c{3} \c{3,6}://(\c{1,6}\.){1,2}\c{3} \c{3,6}://(\c{1,8}\.){1,4}\c{3}",
            "tokens": True,
        }
    )
