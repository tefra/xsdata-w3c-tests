from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    child_1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    child_2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    my_attr: int = field(
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class FooTest(FooType):
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
        }
    )
