from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class Numtype:
    """
    :ivar value:
    :ivar id_1:
    :ivar id_2:
    """
    class Meta:
        name = "numtype"

    value: Optional[int] = field(
        default=None,
    )
    id_1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    id_2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar number:
    """
    class Meta:
        name = "root"
        namespace = "a"

    number: List[Numtype] = field(
        default_factory=list,
        metadata=dict(
            name="Number",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
