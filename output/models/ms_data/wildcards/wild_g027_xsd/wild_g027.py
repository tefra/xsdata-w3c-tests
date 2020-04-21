from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    """
    :ivar any_element:
    """
    class Meta:
        name = "bar"
        namespace = "http://foobar"

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
    :ivar target_namespace_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    target_namespace_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace",
            required=True
        )
    )
