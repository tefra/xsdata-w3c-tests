from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_element:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement",
            type="Element",
            namespace=""
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
