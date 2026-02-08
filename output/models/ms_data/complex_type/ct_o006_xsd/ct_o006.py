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
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
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
    any_attributes: Any = field(
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
