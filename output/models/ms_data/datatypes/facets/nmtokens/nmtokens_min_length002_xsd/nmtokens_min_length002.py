from dataclasses import dataclass, field
from typing import List, Optional


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
            default=None,
            metadata={
                "required": True,
            }
        )
        attr_test: List[str] = field(
            default_factory=list,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "min_length": 2,
                "tokens": True,
            }
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
