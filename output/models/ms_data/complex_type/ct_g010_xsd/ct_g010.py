from dataclasses import dataclass, field
from lxml.etree import QName
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
    :ivar my_element:
    :ivar my_attr:
    :ivar my_attr2:
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
