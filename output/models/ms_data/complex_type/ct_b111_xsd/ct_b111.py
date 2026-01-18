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
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
