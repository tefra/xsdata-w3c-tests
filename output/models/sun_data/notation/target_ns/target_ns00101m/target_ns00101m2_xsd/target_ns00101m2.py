from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "targetNS"


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
        :cvar TEST_PNG:
        """
        TEST_PNG = "test:png"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "targetNS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
