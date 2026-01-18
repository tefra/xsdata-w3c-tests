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
            "max_inclusive": XmlDuration("P2Y3MT2H"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
