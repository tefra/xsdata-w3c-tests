from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:bar"


@dataclass
class Ct:
    class Meta:
        name = "ct"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Elem:
    class Meta:
        name = "elem"
        namespace = "urn:bar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
