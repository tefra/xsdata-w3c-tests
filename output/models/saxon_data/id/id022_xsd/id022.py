from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Para:
    """
    :ivar value:
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
    )
    key: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            min_occurs=0,
            max_occurs=9223372036854775807
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
