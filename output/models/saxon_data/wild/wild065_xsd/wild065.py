from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class G:
    """
    :ivar value:
    """
    class Meta:
        name = "g"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Zing:
    """
    :ivar g:
    :ivar e:
    :ivar f:
    :ivar local_element:
    """
    class Meta:
        name = "zing"

    g: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    f: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )


@dataclass
class Doc(Zing):
    class Meta:
        name = "doc"
