from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    att: None | QName = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(MyType):
    class Meta:
        name = "root"
