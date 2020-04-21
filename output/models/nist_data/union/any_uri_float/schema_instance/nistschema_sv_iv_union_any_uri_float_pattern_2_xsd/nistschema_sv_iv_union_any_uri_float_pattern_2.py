from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-anyURI-float-pattern-2-NS"


@dataclass
class NistschemaSvIvUnionAnyUriFloatPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-anyURI-float-pattern-2"
        namespace = "NISTSchema-SV-IV-union-anyURI-float-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\c{3,6}://(\c{1,11}\.){1,4}\c{3}"
        )
    )
