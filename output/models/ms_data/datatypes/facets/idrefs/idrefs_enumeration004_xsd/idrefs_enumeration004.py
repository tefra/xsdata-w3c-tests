from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    """
    :ivar idrefs_attr:
    :ivar id_attr:
    """
    class Meta:
        name = "foo"

    idrefs_attr: Optional["Foo.IdrefsAttr"] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    id_attr: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    class IdrefsAttr(Enum):
        """
        :cvar FOO:
        :cvar FOO123:
        :cvar FU1:
        """
        FOO = "foo"
        FOO123 = "foo123"
        FU1 = "fu1"


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[Foo] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"