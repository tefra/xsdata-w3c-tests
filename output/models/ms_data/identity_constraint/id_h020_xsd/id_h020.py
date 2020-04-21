from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Kid:
    """
    :ivar val:
    """
    class Meta:
        name = "kid"
        namespace = "myNS.tempuri.org"

    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Uid:
    """
    :ivar val:
    """
    class Meta:
        name = "uid"
        namespace = "myNS.tempuri.org"

    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar uid:
    :ivar kid:
    """
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

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
