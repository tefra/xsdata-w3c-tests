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
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
    )


@dataclass
class Uidtype:
    """
    :ivar iid:
    """
    class Meta:
        name = "uidtype"

    iid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
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

    uid: List[Uidtype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
