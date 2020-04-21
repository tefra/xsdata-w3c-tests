from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    """
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "attRef"

    att1: Optional["AttRef.Att1"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Att1(Enum):
        """
        :cvar AK:
        :cvar AL:
        :cvar AR:
        """
        AK = "AK"
        AL = "AL"
        AR = "AR"


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
