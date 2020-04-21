from dataclasses import dataclass, field
from lxml.etree import QName
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
    any_attributes: Dict[QName, str] = field(
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
    :ivar my_attr1:
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
    my_attr1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr1",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
