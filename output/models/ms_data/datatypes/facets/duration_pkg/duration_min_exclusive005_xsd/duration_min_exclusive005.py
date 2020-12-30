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
            "min_exclusive": Duration("P1Y1MT1H"),
            "max_exclusive": Duration("P2Y3MT2H"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
