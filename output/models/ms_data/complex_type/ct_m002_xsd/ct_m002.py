from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar value:
    :ivar my_attr:
    """
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
    )
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
