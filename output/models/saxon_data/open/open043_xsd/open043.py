from dataclasses import dataclass, field
from typing import List, Optional
from output.models.saxon_data.open.open043_xsd.open043x import Alpha


@dataclass
class Beta:
    class Meta:
        name = "beta"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    a: Optional[Alpha] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[Beta] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "mixed": True,
        }
    )
