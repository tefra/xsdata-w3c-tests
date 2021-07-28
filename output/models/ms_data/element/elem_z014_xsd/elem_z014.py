from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn-klondike-test"


@dataclass
class CtypeFoo:
    class Meta:
        name = "ctype_foo"

    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class RootElem:
    class Meta:
        name = "root_elem"
        namespace = "urn-klondike-test"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
