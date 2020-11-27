from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.publishing.org"


@dataclass
class B:
    class Meta:
        name = "b"
        namespace = "http://www.publishing.org"

    b: Optional["B"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.publishing.org"

    keys: Optional["Root.Keys"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    keyref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Keys:
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 1,
            }
        )
