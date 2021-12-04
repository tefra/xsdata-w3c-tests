from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Elem2:
    class Meta:
        name = "elem2"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Elem3:
    class Meta:
        name = "elem3"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem2: Optional[Elem2] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
