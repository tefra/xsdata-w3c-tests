from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    low_line_hyphen_minus_full_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "_-.",
            "type": "Attribute",
        },
    )
    value_0: Optional[int] = field(
        default=None,
        metadata={
            "name": "_-0.",
            "type": "Attribute",
        },
    )
