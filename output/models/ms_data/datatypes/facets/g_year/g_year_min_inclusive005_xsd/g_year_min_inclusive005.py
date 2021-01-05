from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": XmlPeriod("1998"),
            "max_exclusive": XmlPeriod("2002"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
