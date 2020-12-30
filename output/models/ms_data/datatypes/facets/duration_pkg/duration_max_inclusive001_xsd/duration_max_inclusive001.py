from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Duration


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[Duration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": Duration("P1Y1MT1H"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
