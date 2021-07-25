from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    a: Optional[XmlDate] = field(
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
        }
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
