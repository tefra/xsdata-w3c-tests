from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "max_exclusive": XmlDate(2000, 5, 31),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
