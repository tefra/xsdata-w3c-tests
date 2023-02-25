from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
