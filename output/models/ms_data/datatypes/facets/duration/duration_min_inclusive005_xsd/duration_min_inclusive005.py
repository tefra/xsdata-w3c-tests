from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlDuration("P1Y1MT1H"),
            "max_exclusive": XmlDuration("P2Y3MT2H"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
