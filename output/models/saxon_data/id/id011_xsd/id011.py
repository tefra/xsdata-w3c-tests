from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Para:
    """
    :ivar value:
    :ivar id:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
    )
    id: str = field(
        init=False,
        default="para001",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
