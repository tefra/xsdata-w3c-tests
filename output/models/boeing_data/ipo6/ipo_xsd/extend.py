from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.com/IPO"


@dataclass
class ExternFirstElement:
    class Meta:
        namespace = "http://www.example.com/IPO"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
