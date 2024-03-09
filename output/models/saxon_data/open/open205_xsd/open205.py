from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from output.models.saxon_data.open.open205_xsd.open205x import BType


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
        },
    )
    extra_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
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
        },
    )
    extra_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
    )
    a: Optional[AType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    b: Optional[BType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
