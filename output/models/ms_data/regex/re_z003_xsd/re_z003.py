from dataclasses import dataclass, field
from typing import List


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[\w]"
        )
    )
