from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


@dataclass
class Root:
    """
    :ivar string:
    """
    class Meta:
        name = "root"
        namespace = "a"

    string: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[a-c]"
        )
    )
