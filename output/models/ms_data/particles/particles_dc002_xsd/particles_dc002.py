from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Elem2:
    """
    :ivar any_element:
    """
    class Meta:
        name = "elem2"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Elem3:
    """
    :ivar any_element:
    """
    class Meta:
        name = "elem3"
        namespace = "http://xsdtesting"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Doc:
    """
    :ivar elem2:
    :ivar elem1:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem2: Optional[Elem2] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    elem1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
