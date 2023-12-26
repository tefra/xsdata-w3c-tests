from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    class Meta:
        name = "ids"

    idref_element: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    id_attr: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root(Ids):
    class Meta:
        name = "root"
