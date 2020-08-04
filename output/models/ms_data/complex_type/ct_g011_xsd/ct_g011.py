from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MyType:
    """
    :ivar any_element:
    :ivar any_attributes:
    """
    class Meta:
        name = "myType"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class FooType(MyType):
    """
    :ivar my_element:
    :ivar local_attributes:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
            type="Element",
            namespace="",
            required=True
        )
    )
    local_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
