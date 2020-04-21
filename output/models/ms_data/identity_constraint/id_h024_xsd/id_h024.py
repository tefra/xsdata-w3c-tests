from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Kid:
    """
    :ivar val:
    """
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class UidType:
    """
    :ivar val:
    """
    class Meta:
        name = "uidType"

    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Uid(UidType):
    class Meta:
        name = "uid"



@dataclass
class Uid2(UidType):
    class Meta:
        name = "uid2"



@dataclass
class Root:
    """
    :ivar uid2:
    :ivar uid:
    :ivar kid:
    """
    class Meta:
        name = "root"

    uid2: List[Uid2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    uid: List[Uid] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
