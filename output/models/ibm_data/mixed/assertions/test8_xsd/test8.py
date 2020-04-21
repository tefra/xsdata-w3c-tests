from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ShoeType:
    """
    :ivar value:
    :ivar country:
    """
    class Meta:
        name = "shoeType"

    value: Optional[int] = field(
        default=None,
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Shoesize(ShoeType):
    class Meta:
        name = "shoesize"
