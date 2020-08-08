from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.additional.test66745_a_xsd.test66745_a import Foo1

__NAMESPACE__ = "foo"


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Bar:
    """
    :ivar foo1:
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "bar"
        namespace = "foo"

    foo1: List[Foo1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="foo1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    foo: List[Foo] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    bar: List["Bar"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
