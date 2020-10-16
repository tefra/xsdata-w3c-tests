from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Foo:
    """
    :ivar my_ele1:
    :ivar my_ele2:
    :ivar my_ele3:
    :ivar any_attributes:
    """
    class Meta:
        name = "foo"

    my_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele3: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class FooType:
    """
    :ivar my_ele1:
    :ivar my_ele2:
    :ivar my_ele3:
    :ivar any_attributes:
    :ivar my_attr:
    """
    class Meta:
        name = "fooType"

    my_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_ele3: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
        }
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
    my_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
