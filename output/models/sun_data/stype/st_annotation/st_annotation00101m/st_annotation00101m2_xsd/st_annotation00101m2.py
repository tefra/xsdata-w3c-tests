from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ST_final"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            tokens=True
        )
    )
