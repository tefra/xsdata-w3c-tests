from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[str, Decimal, int]] = field(
        default=None,
    )
