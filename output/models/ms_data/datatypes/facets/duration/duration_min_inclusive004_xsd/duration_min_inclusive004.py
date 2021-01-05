from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": XmlDuration("P1Y1MT1H"),
            "max_inclusive": XmlDuration("P2Y3MT2H"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
