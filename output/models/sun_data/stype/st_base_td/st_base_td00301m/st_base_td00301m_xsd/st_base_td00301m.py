from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ST_baseTD"


@dataclass
class Test:
    """
    :ivar value:
    """
    class Meta:
        name = "test"
        namespace = "ST_baseTD"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )