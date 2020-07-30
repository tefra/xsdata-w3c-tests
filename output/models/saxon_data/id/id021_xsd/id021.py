from dataclasses import dataclass, field
from typing import List


@dataclass
class Para:
    """
    :ivar e:
    """
    class Meta:
        name = "para"

    e: str = field(
        default="entity1 entity2",
        metadata=dict(
            type="Element",
            required=True
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
