from dataclasses import dataclass, field
from enum import Enum
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
        :cvar FOO:
        :cvar HTTP_WWW_MICROSOFT_COM:
        :cvar MAILTO_DAVEBROW_MICROSOFT_COM:
        """
        FOO = "foo"
        HTTP_WWW_MICROSOFT_COM = "http://www.microsoft.com"
        MAILTO_DAVEBROW_MICROSOFT_COM = "mailto:davebrow@microsoft.com"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
