from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Mylist(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Mylist] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
