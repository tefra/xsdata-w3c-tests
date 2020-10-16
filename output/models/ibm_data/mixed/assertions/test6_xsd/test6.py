from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BaseType:
    """
    :ivar body:
    :ivar must_understand:
    """
    class Meta:
        name = "baseType"

    body: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    must_understand: Optional[str] = field(
        default=None,
        metadata={
            "name": "mustUnderstand",
            "type": "Attribute",
        }
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar attr1:
    """
    class Meta:
        name = "derivedType"

    attr1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Message(DerivedType):
    class Meta:
        name = "message"
