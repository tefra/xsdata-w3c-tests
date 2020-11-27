from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[float, Decimal, int]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
