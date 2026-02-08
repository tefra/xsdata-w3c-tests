from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: XmlTime = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlTime(10, 21, 0, 0, -300),
            "max_inclusive": XmlTime(13, 20, 0, 0, -240),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
