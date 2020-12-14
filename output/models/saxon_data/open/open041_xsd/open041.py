from dataclasses import dataclass, field
from typing import List, Optional
from output.models.saxon_data.open.open041_xsd.open041x import Beta


@dataclass
class Alpha:
    class Meta:
        name = "alpha"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    a: Optional[object] = field(
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
