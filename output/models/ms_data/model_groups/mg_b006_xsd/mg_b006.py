from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bar:
    class Meta:
        name = "bar"

    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(Bar):
    class Meta:
        name = "root"
