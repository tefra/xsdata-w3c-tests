from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "required": True,
        }
    )
