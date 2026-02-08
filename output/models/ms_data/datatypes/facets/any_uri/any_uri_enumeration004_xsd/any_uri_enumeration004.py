from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooTypeFoo(Enum):
    FOO = "foo"
    HTTP_WWW_MICROSOFT_COM = "http://www.microsoft.com"
    MAILTO_DAVEBROW_MICROSOFT_COM = "mailto:davebrow@microsoft.com"


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooTypeFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
