from dataclasses import dataclass, field
from typing import Optional


@dataclass
class C2:
    class Meta:
        name = "C"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r".*:00",
        }
    )


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class C1:
    class Meta:
        name = "c"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "required": True,
        }
    )
    other_ns_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://other.ns/",
            "required": True,
        }
    )
