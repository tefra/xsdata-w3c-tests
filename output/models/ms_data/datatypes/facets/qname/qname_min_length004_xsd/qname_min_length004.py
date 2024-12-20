from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 4,
            "max_length": 6,
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
