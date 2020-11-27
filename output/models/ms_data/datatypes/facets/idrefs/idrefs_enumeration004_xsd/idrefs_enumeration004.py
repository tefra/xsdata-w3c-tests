from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: List["Foo.IdrefsAttr"] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    id_attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class IdrefsAttr(Enum):
        FOO = "foo"
        FOO123 = "foo123"
        FU1 = "fu1"


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[Foo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
