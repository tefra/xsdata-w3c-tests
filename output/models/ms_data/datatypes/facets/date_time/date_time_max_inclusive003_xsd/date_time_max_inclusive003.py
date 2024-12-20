from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": XmlDateTime(1999, 5, 12, 10, 31, 0),
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
