from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Child:
    """
    :ivar any_element:
    """
    class Meta:
        name = "child"
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
class MyType:
    """
    :ivar child:
    """
    class Meta:
        name = "myType"

    child: Optional[Child] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


@dataclass
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "foo"
