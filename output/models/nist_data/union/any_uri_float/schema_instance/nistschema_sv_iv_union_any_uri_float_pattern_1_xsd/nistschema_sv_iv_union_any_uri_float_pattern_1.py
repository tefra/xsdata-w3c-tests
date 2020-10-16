from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionAnyUriFloatPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-1"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{1}\.\d{3}E\d{2}",
        }
    )
