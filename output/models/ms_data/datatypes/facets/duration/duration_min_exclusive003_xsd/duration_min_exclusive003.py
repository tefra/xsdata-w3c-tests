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
            "min_exclusive": XmlDuration("P1Y1MT1H"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
