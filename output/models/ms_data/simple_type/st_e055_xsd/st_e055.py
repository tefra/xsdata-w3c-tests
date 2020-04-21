from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[Union[bool, float, Decimal, str]] = field(
        default=None,
    )
