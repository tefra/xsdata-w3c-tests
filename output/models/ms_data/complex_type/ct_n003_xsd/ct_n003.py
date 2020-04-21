from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class Foo:
    """
    :ivar my_ele1:
    :ivar my_ele2:
    :ivar my_ele3:
    :ivar local_attributes:
    """
    class Meta:
        name = "foo"

    my_ele1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myEle1",
            type="Element",
            namespace=""
        )
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata=dict(
            name="myEle2",
            type="Element",
            namespace=""
        )
    )
    my_ele3: Optional[int] = field(
        default=None,
        metadata=dict(
            name="myEle3",
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
class FooType(Foo):
    """
    :ivar my_ele4:
    :ivar any_attributes:
    """
    class Meta:
        name = "fooType"

    my_ele4: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myEle4",
            type="Element",
            namespace="",
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
class Root(FooType):
    class Meta:
        name = "root"
