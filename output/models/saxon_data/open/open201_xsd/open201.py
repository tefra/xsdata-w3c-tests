from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "aType"

    extra_number: None | Decimal = field(
        default=None,
        metadata={
            "name": "extra-number",
            "type": "Attribute",
        },
    )
    extra_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
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
        },
    )
    extra_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "extra-date",
            "type": "Attribute",
        },
    )
    a: AType = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
