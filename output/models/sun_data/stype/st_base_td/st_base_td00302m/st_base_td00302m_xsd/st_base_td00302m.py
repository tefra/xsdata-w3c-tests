from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_baseTD"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_baseTD"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 3,
            "pattern": r"b+",
        }
    )
