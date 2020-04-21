from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BType:
    """
    :ivar att_b:
    """
    class Meta:
        name = "bType"

    att_b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class BsType:
    """
    :ivar b:
    """
    class Meta:
        name = "bsType"

    b: Optional[BType] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )


@dataclass
class AType:
    """
    :ivar bs:
    :ivar c:
    :ivar att_a:
    """
    class Meta:
        name = "aType"

    bs: Optional[BsType] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    c: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    att_a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class RType:
    """
    :ivar a:
    """
    class Meta:
        name = "rType"

    a: List[AType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root(RType):
    class Meta:
        name = "root"
