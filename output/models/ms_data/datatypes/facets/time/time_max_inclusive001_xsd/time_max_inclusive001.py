from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": XmlTime(10, 21, 0, 0, -300),
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
