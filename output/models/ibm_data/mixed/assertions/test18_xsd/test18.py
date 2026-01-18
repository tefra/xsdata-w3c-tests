from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class X:
    a: None | X.A = field(
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
    class A:
        a1: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        a_count: None | int = field(
            default=None,
            metadata={
                "name": "aCount",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Y:
    a: None | Y.A = field(
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
    class A:
        a1: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        a_count: None | int = field(
            default=None,
            metadata={
                "name": "aCount",
                "type": "Attribute",
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
