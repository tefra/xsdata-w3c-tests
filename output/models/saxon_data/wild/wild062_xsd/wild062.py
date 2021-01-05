from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class E:
    class Meta:
        name = "e"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    e: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    f: Optional[str] = field(
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
class Doc(Zing):
    class Meta:
        name = "doc"
