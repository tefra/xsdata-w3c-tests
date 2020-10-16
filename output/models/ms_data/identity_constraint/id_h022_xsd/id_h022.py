from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022_imp import Iid


@dataclass
class Kid:
    """
    :ivar val:
    """
    class Meta:
        name = "kid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Uid:
    """
    :ivar val:
    """
    class Meta:
        name = "uid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar uid:
    :ivar iid:
    :ivar kid:
    """
    class Meta:
        name = "root"

    uid: List[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    iid: List[Iid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "importNS",
        }
    )
    kid: List[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
