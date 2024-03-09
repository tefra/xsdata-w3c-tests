from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": XmlDate(1999, 1, 31),
            "max_inclusive": XmlDate(2000, 5, 31),
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
