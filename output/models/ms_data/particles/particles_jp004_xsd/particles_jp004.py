from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar target_namespace_element:
    """
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##targetNamespace",
            "required": True,
        }
    )


@dataclass
class E1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e1"
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
class R(B):
    """
    :ivar e1:
    """
    e1: Optional[E1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xsdtesting",
            "required": True,
        }
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
