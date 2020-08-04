from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MyType:
    """
    :ivar my_element1:
    :ivar my_element2:
    :ivar my_element3:
    :ivar local_attributes:
    """
    class Meta:
        name = "myType"

    my_element1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement1",
            type="Element",
            namespace=""
        )
    )
    my_element2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement2",
            type="Element",
            namespace=""
        )
    )
    my_element3: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement3",
            type="Element",
            namespace=""
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
class FooType(MyType):
    """
    :ivar my_attr:
    """
    class Meta:
        name = "fooType"

    my_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
