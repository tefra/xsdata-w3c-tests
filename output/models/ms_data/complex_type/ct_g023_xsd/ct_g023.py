from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar my_element1:
    :ivar my_element2:
    :ivar my_element3:
    :ivar any_attributes:
    :ivar local_attributes:
    """
    class Meta:
        name = "fooType"

    my_element1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="myElement1",
            type="Element",
            namespace="",
            required=True
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
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
    local_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class MyType:
    """
    :ivar my_element1:
    :ivar my_element2:
    :ivar my_element3:
    :ivar any_attributes:
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
    any_attributes: Dict = field(
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
