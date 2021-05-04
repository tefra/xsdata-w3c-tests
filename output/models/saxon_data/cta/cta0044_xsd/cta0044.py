from dataclasses import dataclass, field
from typing import Optional

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
        }
    )
    f: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "abc",
        }
    )
    switch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
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


@dataclass
class ATypeT(AType):
    class Meta:
        name = "aType_t"


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
        }
    )
