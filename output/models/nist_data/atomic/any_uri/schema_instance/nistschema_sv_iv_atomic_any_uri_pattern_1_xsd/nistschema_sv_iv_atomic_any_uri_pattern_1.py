from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,7}\.){1,2}\c{3}",
        }
    )
