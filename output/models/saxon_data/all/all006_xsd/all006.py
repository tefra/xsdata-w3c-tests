from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class C1:
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

    value: Optional[XmlTime] = field(
        default=None
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[XmlTime] = field(
        default=None
    )


@dataclass
class C2:
    class Meta:
        name = "c"

    value: Optional[XmlTime] = field(
        default=None
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
        }
    )
    b: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
        }
    )
    other_ns_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://other.ns/",
        }
    )
