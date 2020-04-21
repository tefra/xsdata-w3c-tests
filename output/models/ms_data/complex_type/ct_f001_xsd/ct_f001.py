from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    """
    :ivar my_element:
    """
    class Meta:
        name = "myType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
            type="Element",
            namespace="",
            required=True
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
