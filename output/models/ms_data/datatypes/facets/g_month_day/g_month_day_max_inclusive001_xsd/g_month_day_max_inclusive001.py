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
            "max_inclusive": XmlPeriod("--01-01"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
