from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class ParentType:
    class Meta:
        name = "parentType"



@dataclass
class Ttype:
    """
    :ivar value:
    :ivar col:
    """
    class Meta:
        name = "ttype"

    value: Optional[str] = field(
        default=None,
    )
    col: Optional[str] = field(
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
        namespace = "myNS.tempuri.org"



@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: List[T] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
