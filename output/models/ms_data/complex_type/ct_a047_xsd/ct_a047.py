from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TypeFoo:
    class Meta:
        name = "_foo"

    value: Optional[str] = field(
        default=None,
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(TypeFoo):
    class Meta:
        name = "root"
