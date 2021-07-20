from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,6}\.){1,2}\c{3}",
        }
    )
