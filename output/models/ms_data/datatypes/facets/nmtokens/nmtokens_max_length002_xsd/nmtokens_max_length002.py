from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooType.Foo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Foo:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        attr_test: list[str] = field(
            default_factory=list,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "max_length": 1,
                "tokens": True,
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
