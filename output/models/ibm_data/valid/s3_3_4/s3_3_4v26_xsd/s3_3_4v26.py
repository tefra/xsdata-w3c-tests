from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    idref_element: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id_attr: str = field(
        default="zxc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(Ids):
    class Meta:
        name = "root"
