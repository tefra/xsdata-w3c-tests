from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar value:
    :ivar value_0:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "_-.",
            "type": "Attribute",
        }
    )
    value_0: Optional[int] = field(
        default=None,
        metadata={
            "name": "_-0.",
            "type": "Attribute",
        }
    )
