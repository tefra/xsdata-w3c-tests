from dataclasses import dataclass, field
from lxml.etree import QName
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
    local_attributes: Dict[QName, str] = field(
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
    :ivar my_attr1:
    :ivar my_attr2:
    :ivar my_attr3:
    :ivar my_attr4:
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
    my_attr2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr2",
            type="Attribute"
        )
    )
    my_attr3: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr3",
            type="Attribute"
        )
    )
    my_attr4: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myAttr4",
            type="Attribute"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"