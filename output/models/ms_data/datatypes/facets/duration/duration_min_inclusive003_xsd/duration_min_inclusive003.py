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
            "required": True,
            "min_inclusive": XmlDuration("P1Y1MT1H"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
