from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar uid:
    """
    class Meta:
        name = "root"

    uid: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Uid:
    """
    :ivar value:
    """
    class Meta:
        name = "uid"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
