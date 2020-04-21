from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    """
    :ivar foo_ele1:
    :ivar foo_ele2:
    :ivar foo_ele3:
    """
    class Meta:
        name = "myType"

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
            namespace="",
            required=True
        )
    )


@dataclass
class FooTest(MyType):
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
