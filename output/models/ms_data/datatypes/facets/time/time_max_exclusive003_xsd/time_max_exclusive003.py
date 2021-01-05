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
            "max_exclusive": XmlTime(13, 20, 0, 0, -240),
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
