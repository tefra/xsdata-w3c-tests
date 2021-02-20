from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Restrict(Enum):
    ADS = "ads"


@dataclass
class Root:
    class Meta:
        name = "root"

    a: Restrict = field(
        init=False,
        default=Restrict.ADS,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
