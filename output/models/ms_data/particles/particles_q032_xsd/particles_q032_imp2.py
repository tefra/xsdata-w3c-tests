from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "bar"


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "bar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class E2:
    class Meta:
        name = "e2"
        namespace = "bar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class ImpElem1:
    class Meta:
        name = "impElem1"
        namespace = "bar"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
