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
            "required": True,
            "max_inclusive": XmlPeriod("1998"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
