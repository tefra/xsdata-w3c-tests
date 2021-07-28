from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    evidence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    open_com_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        }
    )
