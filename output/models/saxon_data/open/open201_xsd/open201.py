from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class AType:
    class Meta:
        name = "aType"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
        }
    )
    extra_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
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
        }
    )
    extra_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
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
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
