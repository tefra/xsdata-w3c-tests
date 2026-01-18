from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Mytype1:
    class Meta:
        name = "mytype1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    attr_test1: None | int = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
            "namespace": "a",
        },
    )
    attr_test2: None | str = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
            "namespace": "a",
        },
    )


@dataclass(kw_only=True)
class FooType(Mytype1):
    class Meta:
        name = "fooType"
