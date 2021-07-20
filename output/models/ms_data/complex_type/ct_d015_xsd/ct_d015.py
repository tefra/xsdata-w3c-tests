from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooType(Enum):
    CA = "CA"


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[FooType] = field(
        default=None
    )
