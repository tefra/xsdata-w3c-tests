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
            "min_exclusive": XmlPeriod("--01-01"),
            "max_inclusive": XmlPeriod("--10-01"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
