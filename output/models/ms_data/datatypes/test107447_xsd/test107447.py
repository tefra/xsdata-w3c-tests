from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    token: str = field(
        metadata={
            "type": "Element",
        }
    )
    language: str = field(
        metadata={
            "type": "Element",
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
        }
    )
    ncname: str = field(
        metadata={
            "type": "Element",
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
        }
    )
    idref: str = field(
        metadata={
            "type": "Element",
        }
    )
    idrefs: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
    nmtoken: str = field(
        metadata={
            "type": "Element",
        }
    )
    nmtokens: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
