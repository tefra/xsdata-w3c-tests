from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class A:
    """
    :ivar a1:
    :ivar a2:
    """
    a1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )
    a2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Elem1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "elem1"
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
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"
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
class Elem2(A):
    class Meta:
        name = "elem2"
        namespace = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar elem1:
    :ivar elem2:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem1: Optional[Elem1] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    elem2: Optional[Elem2] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
