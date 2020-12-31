from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import Period


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[Period] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Period("2000-12"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
