from dataclasses import dataclass, field
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
    time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
