from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "b"


@dataclass
class B1:
    """
    :ivar value:
    """
    class Meta:
        name = "b1"
        namespace = "b"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B2:
    """
    :ivar value:
    """
    class Meta:
        name = "b2"
        namespace = "b"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
