from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime


@dataclass(kw_only=True)
class C1:
    class Meta:
        name = "C"

    value: str = field(
        default="",
        metadata={
            "pattern": r".*:00",
        },
    )


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: XmlTime = field()


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"

    value: XmlTime = field()


@dataclass(kw_only=True)
class C2:
    class Meta:
        name = "c"

    value: XmlTime = field()


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    a: XmlDate = field(
        metadata={
            "type": "Element",
        }
    )
    b: B = field(
        metadata={
            "type": "Element",
        }
    )
    target_namespace_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        },
    )
    other_ns_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://other.ns/",
        },
    )
