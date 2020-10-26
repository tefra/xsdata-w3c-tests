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
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
    )
    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "required": True,
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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
    :ivar t_or_u:
    """
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t_or_u: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "t",
                    "type": T,
                },
                {
                    "name": "u",
                    "type": U,
                },
            ),
        }
    )
