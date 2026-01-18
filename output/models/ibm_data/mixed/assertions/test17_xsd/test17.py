from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class X:
    a: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    d: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Y:
    a: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    b: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    c: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    d: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    x: X = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y: Y = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
