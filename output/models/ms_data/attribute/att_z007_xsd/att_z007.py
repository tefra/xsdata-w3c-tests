from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class One:
    elem1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    elem2: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    att1: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Two(One):
    elem1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    elem2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    att1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Three(Two):
    att1: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    e1: One = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e2: Two = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e3: Three = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
