from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "fooEle1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    foo_ele2: Optional[int] = field(
        default=None,
        metadata={
            "name": "fooEle2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class MyType(FooType):
    class Meta:
        name = "myType"

    foo_ele3: Optional[bool] = field(
        default=None,
        metadata={
            "name": "fooEle3",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class FooTest(MyType):
    class Meta:
        name = "fooTest"


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
