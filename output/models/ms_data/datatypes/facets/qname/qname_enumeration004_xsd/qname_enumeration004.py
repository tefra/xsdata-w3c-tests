from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName


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

    class Foo(Enum):
        FOO_FO = QName("{myNamespace}fo")
        FOO_FOO123 = QName("{myNamespace}foo123")
        FOO_FU1 = QName("{myNamespace}fu1")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
