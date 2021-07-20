from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Foo:
        value: Optional[str] = field(
            default=None
        )
        attr_test: Optional[str] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "min_length": 5,
            }
        )
        id_attr: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
