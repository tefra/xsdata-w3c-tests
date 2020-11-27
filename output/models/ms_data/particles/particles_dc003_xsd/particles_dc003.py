from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Elem1:
    class Meta:
        name = "elem1"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


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
            "required": True,
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
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem3: Optional[Elem3] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    elem2: Optional[Elem2] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    elem1: Optional[Elem1] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
