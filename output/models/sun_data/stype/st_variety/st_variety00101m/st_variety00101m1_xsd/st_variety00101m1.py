from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ST_final"


@dataclass
class Test:
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 2,
            "pattern": r"1*",
        }
    )
