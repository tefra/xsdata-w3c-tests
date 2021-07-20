from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,7}\.){1,4}\c{3}",
        }
    )
