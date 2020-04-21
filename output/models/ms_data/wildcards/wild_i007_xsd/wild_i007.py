from dataclasses import dataclass, field
from typing import List, Optional

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
    :ivar target_namespace_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    other_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            min_occurs=0,
            max_occurs=10
        )
    )
    target_namespace_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace",
            min_occurs=0,
            max_occurs=10
        )
    )
