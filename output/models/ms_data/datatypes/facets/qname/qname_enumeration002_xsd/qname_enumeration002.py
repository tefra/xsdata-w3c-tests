from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName


class FooTypeFoo(Enum):
    FOO_FO = QName("{myNamespace}fo")


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[FooTypeFoo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
