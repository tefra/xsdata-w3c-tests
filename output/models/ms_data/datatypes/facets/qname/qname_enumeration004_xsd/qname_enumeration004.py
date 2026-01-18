from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName


class FooTypeFoo(Enum):
    FOO_FO = QName("{myNamespace}fo")
    FOO_FOO123 = QName("{myNamespace}foo123")
    FOO_FU1 = QName("{myNamespace}fu1")


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooTypeFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
