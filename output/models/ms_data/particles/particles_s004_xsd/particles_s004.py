from dataclasses import dataclass, field
from typing import Optional, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Address:
    class Meta:
        name = "address"

    street: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    zip: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class E3:
    class Meta:
        name = "e3"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class B:
    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e2: Optional[Address] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    e3: Optional[E3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
        },
    )


@dataclass
class R(B):
    e3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
