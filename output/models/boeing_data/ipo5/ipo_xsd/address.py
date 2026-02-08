from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.example.com/add"


@dataclass(kw_only=True)
class AddressType:
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
        }
    )
    street: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
        }
    )
    city: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.example.com/add",
        }
    )
