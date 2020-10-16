from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Restrict(Enum):
    """
    :cvar ADS:
    """
    ADS = "ads"


@dataclass
class Root:
    """
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "root"

    a: Restrict = field(
        init=False,
        default=Restrict.ADS,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
