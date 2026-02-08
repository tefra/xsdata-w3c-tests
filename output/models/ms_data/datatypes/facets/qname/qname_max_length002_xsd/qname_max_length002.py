from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: QName = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "max_length": 5,
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
