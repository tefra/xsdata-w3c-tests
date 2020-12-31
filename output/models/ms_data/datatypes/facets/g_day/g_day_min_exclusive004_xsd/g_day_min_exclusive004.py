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
            "min_exclusive": Period("---01"),
            "max_inclusive": Period("---30"),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
