from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: Optional["Foo.IdrefsAttr"] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
