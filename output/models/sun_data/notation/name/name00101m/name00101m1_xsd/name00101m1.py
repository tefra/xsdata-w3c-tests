from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "name"


@dataclass
class Picture:
    """
    :ivar type:
    """
    type: Optional["Picture.Type"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class Type(Enum):
        """
        :cvar PNG:
        """
        PNG = "png"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "name"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )