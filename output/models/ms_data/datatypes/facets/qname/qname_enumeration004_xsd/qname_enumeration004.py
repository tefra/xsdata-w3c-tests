from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    class Foo(Enum):
        """
        :cvar FOO_FO:
        :cvar FOO_FOO123:
        :cvar FOO_FU1:
        """
        FOO_FO = QName("myNamespace", "fo")
        FOO_FOO123 = QName("myNamespace", "foo123")
        FOO_FU1 = QName("myNamespace", "fu1")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
