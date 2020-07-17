from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    """
    :ivar content:
    :ivar row:
    :ivar ref:
    :ivar col:
    """
    class Meta:
        name = "ttype"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    row: List["Ttype.Row"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="myNS.tempuri.org",
            min_occurs=1,
            max_occurs=10,
            sequential=True
        )
    )
    ref: List["Ttype.Ref"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="myNS.tempuri.org",
            min_occurs=1,
            max_occurs=10,
            sequential=True
        )
    )
    col: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="myNS.tempuri.org"
        )
    )

    @dataclass
    class Row:
        """
        :ivar value:
        :ivar x:
        """
        value: Optional[str] = field(
            default=None,
        )
        x: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                namespace="myNS.tempuri.org"
            )
        )

    @dataclass
    class Ref:
        """
        :ivar value:
        :ivar y:
        """
        value: Optional[str] = field(
            default=None,
        )
        y: Optional[str] = field(
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
