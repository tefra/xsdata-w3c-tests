from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Bar:
    """
    :ivar any_element:
    """
    class Meta:
        name = "bar"
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
    :ivar other_element:
    :ivar a_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )
    a_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="A",
            required=True
        )
    )