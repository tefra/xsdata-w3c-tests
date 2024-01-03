from dataclasses import dataclass, field
from typing import Optional, Any

__NAMESPACE__ = "abc"


@dataclass
class AType:
    class Meta:
        name = "aType"

    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
        },
    )
    f: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
        },
    )
    switch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class A(AType):
    class Meta:
        name = "a"
        namespace = "abc"


@dataclass
class ATypeF(AType):
    class Meta:
        name = "aType_f"

    t: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    f: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
            "required": True,
        },
    )
    r: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ATypeT(AType):
    class Meta:
        name = "aType_t"

    f: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
            "required": True,
        },
    )


@dataclass
class Top:
    class Meta:
        name = "top"
        namespace = "abc"

    a: Optional[A] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
