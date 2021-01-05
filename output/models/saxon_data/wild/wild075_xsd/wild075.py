from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class B:
    class Meta:
        name = "b"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
