from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AType:
    """
    :ivar extra_number:
    :ivar extra_date:
    """
    class Meta:
        name = "aType"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="extra-number",
            type="Attribute"
        )
    )
    extra_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="extra-date",
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar extra_number:
    :ivar extra_date:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "doc"

    extra_number: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="extra-number",
            type="Attribute"
        )
    )
    extra_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="extra-date",
            type="Attribute"
        )
    )
    a: Optional[AType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    c: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )