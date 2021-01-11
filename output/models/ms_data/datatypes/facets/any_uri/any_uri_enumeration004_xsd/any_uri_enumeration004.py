from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooTypeFoo(Enum):
    FOO = "foo"
    HTTP_WWW_MICROSOFT_COM = "http://www.microsoft.com"
    MAILTO_DAVEBROW_MICROSOFT_COM = "mailto:davebrow@microsoft.com"


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[FooTypeFoo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
