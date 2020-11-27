from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "str00Aー",
            "type": "Attribute",
        }
    )
    str10: Optional[str] = field(
        default=None,
        metadata={
            "name": "str10-ヽ",
            "type": "Attribute",
        }
    )
    str20: Optional[str] = field(
        default=None,
        metadata={
            "name": "str20ヾ",
            "type": "Attribute",
        }
    )
