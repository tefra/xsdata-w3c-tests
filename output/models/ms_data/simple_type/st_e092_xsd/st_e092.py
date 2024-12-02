from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union


@dataclass
class Root:
    class Meta:
        name = "root"

    value: list[Union[float, Decimal, int]] = field(
        init=False,
        default_factory=lambda: [
            12,
            1.278656273654,
            4.0,
        ],
        metadata={
            "tokens": True,
        },
    )
