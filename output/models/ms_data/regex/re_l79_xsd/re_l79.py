from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\p{IsCJKCompatibilityIdeographs}+"
        )
    )
