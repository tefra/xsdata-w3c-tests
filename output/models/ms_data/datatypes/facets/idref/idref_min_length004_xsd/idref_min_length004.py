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
        attr_test: None | str = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "min_length": 4,
                "max_length": 6,
            },
        )
        id_attr: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
