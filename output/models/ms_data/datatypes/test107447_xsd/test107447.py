from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    token: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    ncname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    idrefs: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
    nmtoken: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    nmtokens: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
