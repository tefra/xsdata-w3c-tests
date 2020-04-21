from dataclasses import dataclass, field
from typing import List


@dataclass
class Root:
    """
    :ivar r:
    """
    class Meta:
        name = "root"

    r: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=10,
            pattern=r"[ae-]x"
        )
    )
