from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseType:
    class Meta:
        name = "baseType"

    body: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    must_understand: Optional[str] = field(
        default=None,
        metadata={
            "name": "mustUnderstand",
            "type": "Attribute",
        },
    )


@dataclass
class DerivedType(BaseType):
    class Meta:
        name = "derivedType"

    attr1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Message(DerivedType):
    class Meta:
        name = "message"
