from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
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
    must_understand: None | str = field(
        default=None,
        metadata={
            "name": "mustUnderstand",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DerivedType(BaseType):
    class Meta:
        name = "derivedType"

    attr1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Message(DerivedType):
    class Meta:
        name = "message"
