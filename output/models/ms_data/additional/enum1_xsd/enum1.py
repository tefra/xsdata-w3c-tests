from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class EnumType(Enum):
    """
    :cvar VALUE:
    """
    VALUE = "Ѐvalue"


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar att:
    """
    class Meta:
        name = "doc"

    foo: Optional[EnumType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    att: Optional[EnumType] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )