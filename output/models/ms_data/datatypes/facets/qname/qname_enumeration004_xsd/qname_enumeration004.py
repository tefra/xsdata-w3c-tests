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
        :cvar QNAME_MY_NAMESPACE_FO:
        :cvar QNAME_MY_NAMESPACE_FOO123:
        :cvar QNAME_MY_NAMESPACE_FU1:
        """
        QNAME_MY_NAMESPACE_FO = QName("myNamespace", "fo")
        QNAME_MY_NAMESPACE_FOO123 = QName("myNamespace", "foo123")
        QNAME_MY_NAMESPACE_FU1 = QName("myNamespace", "fu1")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"