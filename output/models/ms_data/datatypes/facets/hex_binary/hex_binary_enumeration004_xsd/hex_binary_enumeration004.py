from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooTypeFoo(Enum):
    ADF789 = b"\xad\xf7\x89"
    ABCEDF = b"\xab\xce\xdf"
    VALUE_0123456789 = b"\x01#Eg\x89"


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooTypeFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "format": "base16",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
