from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooIdrefsAttr(Enum):
    FOO = "foo"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: Optional[FooIdrefsAttr] = field(
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
