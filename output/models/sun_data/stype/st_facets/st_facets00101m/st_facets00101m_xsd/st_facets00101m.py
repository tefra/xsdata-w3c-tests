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
        metadata=dict(
            required=True,
            pattern=r"1*"
        )
    )
