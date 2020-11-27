from dataclasses import dataclass, field
from enum import Enum
from typing import List


class U3(Enum):
    X = "x"
    Y = "y"
    VALUE_1 = "1"


@dataclass
class Root:
    class Meta:
        name = "root"

    c: List[U3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 40,
        }
    )
