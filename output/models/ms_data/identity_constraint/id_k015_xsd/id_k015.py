from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class Uid:
    """
    :ivar pid:
    :ivar val:
    :ivar val2:
    """
    class Meta:
        name = "uid"

    pid: List["Uid.Value"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Value(Enum):
        """
        :cvar SMALL:
        :cvar MEDIUM:
        :cvar LARGE:
        """
        SMALL = "small"
        MEDIUM = "medium"
        LARGE = "large"


@dataclass
class Root:
    """
    :ivar uid:
    """
    class Meta:
        name = "root"

    uid: List[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
