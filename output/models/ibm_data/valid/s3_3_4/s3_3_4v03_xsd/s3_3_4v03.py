from enum import Enum
from dataclasses import dataclass, field
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
        default="ads",
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )