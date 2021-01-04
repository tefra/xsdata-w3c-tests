from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Union[bool, float, Decimal, str] = field(
        init=False,
        default=1.0,
    )
