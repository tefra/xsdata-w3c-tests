from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar number:
    """
    class Meta:
        name = "root"
        namespace = "a"

    number: List[int] = field(
        default_factory=list,
        metadata=dict(
            name="Number",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
