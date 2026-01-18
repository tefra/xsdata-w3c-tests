from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo_ele1: str = field(
        metadata={
            "name": "fooEle1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    foo_ele2: int = field(
        metadata={
            "name": "fooEle2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MyType(FooType):
    class Meta:
        name = "myType"

    foo_ele3: bool = field(
        metadata={
            "name": "fooEle3",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FooTest(MyType):
    class Meta:
        name = "fooTest"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
