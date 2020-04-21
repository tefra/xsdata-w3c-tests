from dataclasses import dataclass, field
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
        metadata=dict(
            type="Attribute",
            namespace="myNS.tempuri.org"
        )
    )


@dataclass
class Utype:
    """
    :ivar value:
    :ivar row:
    """
    class Meta:
        name = "utype"

    value: Optional[int] = field(
        default=None,
    )
    row: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="myNS.tempuri.org"
        )
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
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    u: List[U] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
