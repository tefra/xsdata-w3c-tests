from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-3-NS"


@dataclass
class NistschemaSvIvUnionAnyUriFloatPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-3"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\c{3,6}://(\c{1,4}\.){1,4}\c{3}",
        }
    )
