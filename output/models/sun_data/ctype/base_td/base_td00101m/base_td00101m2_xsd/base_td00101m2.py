from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "baseTD"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "baseTD"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
