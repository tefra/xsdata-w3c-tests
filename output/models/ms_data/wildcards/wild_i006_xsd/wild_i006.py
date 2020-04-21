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
    :ivar a_element:
    :ivar b_element:
    :ivar target_namespace_element:
    :ivar local_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://xsdtesting"

    a_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="a",
            min_occurs=0,
            max_occurs=10
        )
    )
    b_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="b",
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
    local_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##local",
            min_occurs=0,
            max_occurs=10
        )
    )
