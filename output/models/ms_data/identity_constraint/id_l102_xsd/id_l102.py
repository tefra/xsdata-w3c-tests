from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    """
    :ivar value:
    :ivar row:
    """
    class Meta:
        name = "ttype"

    value: Optional[bool] = field(
        default=None,
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
    )


@dataclass
class Utype:
    """
    :ivar value:
    :ivar row:
    """
    class Meta:
        name = "utype"

    value: Optional[Decimal] = field(
        default=None,
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
    )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass
class U(Utype):
    class Meta:
        name = "u"
        nillable = True
        namespace = "myNS.tempuri.org"


@dataclass
class Root:
    """
    :ivar t:
    :ivar u:
    """
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    u: List[U] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
