from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    token: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    language: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ncname: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    idref: str = field(
        metadata={
            "type": "Element",
            "required": True,
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
            "required": True,
        }
    )
    nmtokens: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
