from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Bar:
    """
    :ivar any_element:
    """
    class Meta:
        name = "bar"

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
    :ivar foo_element:
    :ivar a_element:
    :ivar b_element:
    :ivar target_namespace_element:
    :ivar local_element:
    :ivar other_element:
    """
    class Meta:
        name = "foo"

    foo_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="foo",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    a_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="a",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    b_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="b",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    target_namespace_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##targetNamespace",
            required=True
        )
    )
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local",
            required=True
        )
    )
    other_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##other",
            required=True
        )
    )
