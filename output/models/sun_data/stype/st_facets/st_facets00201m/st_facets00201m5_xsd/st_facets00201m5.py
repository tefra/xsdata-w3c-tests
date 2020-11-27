from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_facets"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_facets"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -11,
        }
    )
