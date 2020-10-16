from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Kid:
    """
    :ivar val:
    """
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Uid:
    """
    :ivar val:
    :ivar val2:
    """
    class Meta:
        name = "uid"

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


@dataclass
class Root:
    """
    :ivar uid:
    :ivar kid:
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
    kid: List[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
