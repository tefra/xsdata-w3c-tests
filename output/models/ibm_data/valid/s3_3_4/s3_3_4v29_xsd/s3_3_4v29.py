from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    idref_element1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    idref_element2: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id1: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        },
    )
    id2: str = field(
        default="xyz",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    multiple_ids: Ids = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
