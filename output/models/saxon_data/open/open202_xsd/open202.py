from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class AType:
    class Meta:
        name = "aType"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
        }
    )
    extra_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
        }
    )
    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
