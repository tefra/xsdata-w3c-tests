from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CType:
    """
    :ivar att_c:
    """
    class Meta:
        name = "cType"

    att_c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class CsType:
    """
    :ivar c:
    """
    class Meta:
        name = "csType"

    c: Optional[CType] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )


@dataclass
class BType:
    """
    :ivar cs:
    :ivar att_b:
    """
    class Meta:
        name = "bType"

    cs: List[CsType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=11
        )
    )
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

    b: List[BType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=11
        )
    )


@dataclass
class AType:
    """
    :ivar bs:
    :ivar cs:
    :ivar att_a:
    """
    class Meta:
        name = "aType"

    bs: List[BsType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=11
        )
    )
    cs: Optional[CsType] = field(
        default=None,
        metadata=dict(
            type="Element"
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
