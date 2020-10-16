from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "foo"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[b|c]+",
        }
    )
