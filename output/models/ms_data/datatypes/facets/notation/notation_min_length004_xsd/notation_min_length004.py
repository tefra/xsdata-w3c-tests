from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName


class BuildNotation(Enum):
    JPEG = QName("jpeg")
    MPEG = QName("mpeg")
    G = QName("g")


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass
    class Foo:
        value: Optional[str] = field(
            default=None
        )
        attr_test: Optional[BuildNotation] = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "min_length": 3,
                "max_length": 5,
            }
        )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
