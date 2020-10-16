from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar str00_a:
    :ivar str10:
    :ivar str20:
    :ivar str01_a:
    :ivar str02_a:
    :ivar str12:
    :ivar str22:
    :ivar str03_a:
    :ivar str04_a:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str00A⃐",
            "type": "Attribute",
        }
    )
    str10: Optional[str] = field(
        default=None,
        metadata={
            "name": "str10-⃖",
            "type": "Attribute",
        }
    )
    str20: Optional[str] = field(
        default=None,
        metadata={
            "name": "str20⃜",
            "type": "Attribute",
        }
    )
    str01_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str01A⃡",
            "type": "Attribute",
        }
    )
    str02_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str02A〪",
            "type": "Attribute",
        }
    )
    str12: Optional[str] = field(
        default=None,
        metadata={
            "name": "str12-〬",
            "type": "Attribute",
        }
    )
    str22: Optional[str] = field(
        default=None,
        metadata={
            "name": "str22〯",
            "type": "Attribute",
        }
    )
    str03_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str03A゙",
            "type": "Attribute",
        }
    )
    str04_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str04A゚",
            "type": "Attribute",
        }
    )
