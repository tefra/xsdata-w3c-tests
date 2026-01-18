from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate

from output.models.saxon_data.open.open205_xsd.open205x import BType


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "aType"

    extra_number: None | Decimal = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
    )
    extra_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    extra_number: None | Decimal = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
    )
    extra_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
            "namespace": "http://open205x.com/",
        },
    )
    a: AType = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: BType = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    c: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
