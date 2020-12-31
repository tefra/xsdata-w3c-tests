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
            "max_exclusive": Period("--10-01"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
