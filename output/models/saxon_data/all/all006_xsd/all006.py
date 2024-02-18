from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class C1:
    class Meta:
        name = "C"

    value: str = field(
        default="",
        metadata={
            "pattern": r".*:00",
        },
    )


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class C2:
    class Meta:
        name = "c"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    b: Optional[B] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )
    other_ns_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://other.ns/",
        },
    )
