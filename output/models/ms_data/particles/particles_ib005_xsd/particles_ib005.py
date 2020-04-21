from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


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
class Base:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "base"

    foo: List[Foo] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting",
            min_occurs=0,
            max_occurs=4
        )
    )
    bar: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    foo: List[Foo] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    bar: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
