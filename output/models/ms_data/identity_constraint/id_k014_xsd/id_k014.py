from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Uid:
    """
    :ivar pid:
    :ivar val:
    :ivar val2:
    """
    class Meta:
        name = "uid"

    pid: List[List[str]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            tokens=True
        )
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    val2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar uid:
    """
    class Meta:
        name = "root"

    uid: List[Uid] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
