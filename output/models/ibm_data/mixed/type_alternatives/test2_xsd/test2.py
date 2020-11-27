from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class XDecimal:
    class Meta:
        name = "X_Decimal"

    value: Optional[Decimal] = field(
        default=None,
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class XInt:
    class Meta:
        name = "X_Int"

    value: Optional[int] = field(
        default=None,
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class XString:
    class Meta:
        name = "X_String"

    value: Optional[str] = field(
        default=None,
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Example:
    x: List[Union[XDecimal, XInt, XString]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
