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
            "required": True,
            "min_exclusive": XmlDate(1999, 1, 31),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
