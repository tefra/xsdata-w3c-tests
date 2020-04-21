from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar number00:
    :ivar number01:
    :ivar number02:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    number00: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number00_",
            type="Attribute"
        )
    )
    number01: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number01.",
            type="Attribute"
        )
    )
    number02: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number02-",
            type="Attribute"
        )
    )
