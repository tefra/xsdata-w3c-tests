from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\c{3,6}://(\c{1,10}\.){1,5}\c{3}",
        }
    )
