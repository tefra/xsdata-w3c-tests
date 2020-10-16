from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "2002-02-28",
        }
    )
