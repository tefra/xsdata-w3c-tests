from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    attr_test1: None | object = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
        },
    )
    attr_test2: None | object = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        },
    )
    attr_test3: None | object = field(
        default=None,
        metadata={
            "name": "attrTest3",
            "type": "Attribute",
        },
    )
    attr_test4: None | object = field(
        default=None,
        metadata={
            "name": "attrTest4",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
