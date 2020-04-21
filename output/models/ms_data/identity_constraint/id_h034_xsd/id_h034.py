from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ctype:
    """
    :ivar content:
    :ivar val:
    """
    class Meta:
        name = "ctype"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Ctype2(Ctype):
    """
    :ivar content:
    :ivar val2:
    """
    class Meta:
        name = "ctype2"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    val2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Tabletype:
    """
    :ivar c:
    :ivar r:
    """
    class Meta:
        name = "tabletype"

    c: Optional[Ctype] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
