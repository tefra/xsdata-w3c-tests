from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "_foo"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    attr_test: Optional[str] = field(
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
