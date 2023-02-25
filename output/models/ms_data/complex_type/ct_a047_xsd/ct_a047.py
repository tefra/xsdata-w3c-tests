from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "_foo"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
