from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "systemId"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "systemId"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
