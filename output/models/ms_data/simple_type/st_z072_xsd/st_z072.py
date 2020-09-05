from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Mylist(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[Mylist] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
