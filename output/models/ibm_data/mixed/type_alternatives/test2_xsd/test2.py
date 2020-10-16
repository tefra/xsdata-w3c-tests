from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional, Union


@dataclass
class XDecimal:
    """
    :ivar value:
    :ivar kind:
    """
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
    """
    :ivar value:
    :ivar kind:
    """
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
    """
    :ivar value:
    :ivar kind:
    """
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
    """
    :ivar x:
    """
    x: List[Union[XDecimal, XInt, XString]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
