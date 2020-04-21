from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    """
    :ivar my_element:
    :ivar my_element2:
    :ivar my_attr:
    """
    class Meta:
        name = "myType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
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
    my_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr",
            type="Attribute"
        )
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"



@dataclass
class Root(FooType):
    class Meta:
        name = "root"
