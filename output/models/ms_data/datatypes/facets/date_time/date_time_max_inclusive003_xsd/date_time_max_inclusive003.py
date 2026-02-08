from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: XmlDateTime = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "max_inclusive": XmlDateTime(1999, 5, 12, 10, 31, 0),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
