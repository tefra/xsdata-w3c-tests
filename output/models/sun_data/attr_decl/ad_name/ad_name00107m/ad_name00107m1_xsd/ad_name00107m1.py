from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar number00:
    :ivar number10:
    :ivar number20:
    :ivar number01:
    :ivar number02:
    :ivar number12:
    :ivar number22:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    number00: Optional[int] = field(
        default=None,
        metadata={
            "name": "number00一",
            "type": "Attribute",
        }
    )
    number10: Optional[int] = field(
        default=None,
        metadata={
            "name": "number10盒",
            "type": "Attribute",
        }
    )
    number20: Optional[int] = field(
        default=None,
        metadata={
            "name": "number20龥",
            "type": "Attribute",
        }
    )
    number01: Optional[int] = field(
        default=None,
        metadata={
            "name": "number01〇",
            "type": "Attribute",
        }
    )
    number02: Optional[int] = field(
        default=None,
        metadata={
            "name": "number02〡",
            "type": "Attribute",
        }
    )
    number12: Optional[int] = field(
        default=None,
        metadata={
            "name": "number12〥",
            "type": "Attribute",
        }
    )
    number22: Optional[int] = field(
        default=None,
        metadata={
            "name": "number22〩",
            "type": "Attribute",
        }
    )
