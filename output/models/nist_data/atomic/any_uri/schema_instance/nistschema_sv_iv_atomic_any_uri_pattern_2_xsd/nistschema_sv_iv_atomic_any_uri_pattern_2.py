from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,3}\.){1,4}\c{3}",
        }
    )
