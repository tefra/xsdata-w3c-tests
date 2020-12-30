from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "compositor"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time_value: Optional[time] = field(
        default=None,
        metadata={
            "name": "time",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
