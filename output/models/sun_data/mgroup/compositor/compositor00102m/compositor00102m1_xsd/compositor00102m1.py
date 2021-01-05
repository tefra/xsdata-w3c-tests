from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "compositor"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "compositor"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
