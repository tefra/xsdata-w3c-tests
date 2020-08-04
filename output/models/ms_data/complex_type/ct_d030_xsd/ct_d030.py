from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MyType:
    """
    :ivar value:
    :ivar any_attributes:
    """
    class Meta:
        name = "myType"

    value: Optional[str] = field(
        default=None,
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
    :ivar my_attr:
    :ivar my_attr2:
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
    my_attr2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr2",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
