from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    """
    :ivar row:
    :ivar col:
    """
    class Meta:
        name = "ttype"

    row: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="myNS.tempuri.org",
            required=True
        )
    )
    col: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Utype:
    """
    :ivar row:
    :ivar width:
    """
    class Meta:
        name = "utype"

    row: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="myNS.tempuri.org",
            required=True
        )
    )
    width: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"



@dataclass
class U(Utype):
    class Meta:
        name = "u"
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
