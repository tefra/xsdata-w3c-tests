from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class C:
    class Meta:
        name = "c"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class D:
    class Meta:
        name = "d"
        namespace = "a"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class T:
    class Meta:
        name = "t"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
