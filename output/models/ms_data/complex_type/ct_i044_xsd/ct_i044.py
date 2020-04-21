from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar foo_ele1:
    :ivar foo_ele2:
    :ivar foo_ele3:
    :ivar other_attributes:
    """
    class Meta:
        name = "fooType"

    foo_ele1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fooEle1",
            type="Element",
            namespace="",
            required=True
        )
    )
    foo_ele2: Optional[int] = field(
        default=None,
        metadata=dict(
            name="fooEle2",
            type="Element",
            namespace="",
            required=True
        )
    )
    foo_ele3: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="fooEle3",
            type="Element",
            namespace=""
        )
    )
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class MyType:
    """
    :ivar foo_ele1:
    :ivar foo_ele2:
    :ivar foo_ele3:
    :ivar other_attributes:
    """
    class Meta:
        name = "myType"

    foo_ele1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fooEle1",
            type="Element",
            namespace="",
            required=True,
            max_length=4.0
        )
    )
    foo_ele2: Optional[int] = field(
        default=None,
        metadata=dict(
            name="fooEle2",
            type="Element",
            namespace="",
            required=True
        )
    )
    foo_ele3: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="fooEle3",
            type="Element",
            namespace=""
        )
    )
    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )


@dataclass
class FooTest(FooType):
    class Meta:
        name = "fooTest"


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True
        )
    )
