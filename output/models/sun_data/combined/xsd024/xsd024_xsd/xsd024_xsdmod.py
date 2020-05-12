from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foo.com"


class SimpleType(Enum):
    """
    :cvar YES:
    :cvar NO:
    """
    YES = "yes"
    NO = "no"


@dataclass
class ComplexType:
    """
    :ivar root:
    :ivar att:
    """
    class Meta:
        name = "complexType"

    root: Optional["Root"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://foo.com"
        )
    )
    att: Optional[SimpleType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://foo.com"
        )
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "http://foo.com"
