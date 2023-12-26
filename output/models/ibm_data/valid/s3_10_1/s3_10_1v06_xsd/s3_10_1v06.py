from dataclasses import dataclass, field
from typing import List, Optional

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

    d_or_b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "d",
                    "type": int,
                    "namespace": "a",
                },
                {
                    "name": "b",
                    "type": int,
                    "namespace": "a",
                },
            ),
        },
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )


@dataclass
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
