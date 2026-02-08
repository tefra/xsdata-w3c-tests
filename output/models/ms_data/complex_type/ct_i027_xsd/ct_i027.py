from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    my_ele1: None | str = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
        },
    )
    my_ele2: None | int = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        },
    )
    my_ele3: None | int = field(
        default=None,
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class FooType(Foo):
    class Meta:
        name = "fooType"

    my_ele3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    my_ele1: str = field(
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele2: int = field(
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
