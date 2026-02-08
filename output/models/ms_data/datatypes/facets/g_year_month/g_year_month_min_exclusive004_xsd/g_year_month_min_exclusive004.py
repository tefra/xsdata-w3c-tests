from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: XmlPeriod = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_exclusive": XmlPeriod("2000-12"),
            "max_inclusive": XmlPeriod("2001-12"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
