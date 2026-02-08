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
        }
    )

    @dataclass(kw_only=True)
    class Foo:
        value: str = field(default="")
        attr_test: None | str = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "pattern": r"[a-z]{3}",
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
