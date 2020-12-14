from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class AType:
    class Meta:
        name = "aType"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        }
    )
    extra_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        }
    )
    extra_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        }
    )
    a: Optional[AType] = field(
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
            "required": True,
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
