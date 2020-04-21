from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Para:
    """
    :ivar value:
    :ivar id_one:
    :ivar id_two:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
    )
    id_one: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id-one",
            type="Attribute"
        )
    )
    id_two: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id-two",
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
