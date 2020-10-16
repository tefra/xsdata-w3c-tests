from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Root:
    """
    :ivar t:
    :ivar u:
    """
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    u: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class T:
    """
    :ivar value:
    """
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class U:
    """
    :ivar value:
    """
    class Meta:
        name = "u"
        namespace = "myNS.tempuri.org"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
