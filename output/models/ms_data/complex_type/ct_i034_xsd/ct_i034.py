from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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
    foo_ele3: None | bool = field(
        default=None,
        metadata={
            "name": "fooEle3",
            "type": "Element",
            "namespace": "",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class FooTest(FooType):
    class Meta:
        name = "fooTest"


@dataclass(kw_only=True)
class MyType(FooType):
    class Meta:
        name = "myType"

    foo_ele3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


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
