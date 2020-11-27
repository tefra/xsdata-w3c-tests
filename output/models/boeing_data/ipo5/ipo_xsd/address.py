from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.com/add"


@dataclass
class AddressType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
            "required": True,
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
            "required": True,
        }
    )
