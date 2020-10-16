from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


@dataclass
class Foo:
    """
    :ivar idrefs_attr:
    :ivar id_attr:
    """
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
        """
        :cvar FOO:
        """
        FOO = "foo"


@dataclass
class FooType:
    """
    :ivar foo:
    """
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
