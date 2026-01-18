from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Nillable1:
    class Meta:
        name = "nillable1"
        nillable = True
        namespace = "foo"

    x: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Nillable2:
    class Meta:
        name = "nillable2"
        nillable = True
        namespace = "foo"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "min_length": 2,
            "nillable": True,
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class NonNillable:
    class Meta:
        name = "non-nillable"
        namespace = "foo"

    x: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    non_nillable_or_nillable1_or_nillable2: list[
        NonNillable | Nillable1 | Nillable2
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "non-nillable",
                    "type": NonNillable,
                },
                {
                    "name": "nillable1",
                    "type": Nillable1,
                    "nillable": True,
                },
                {
                    "name": "nillable2",
                    "type": Nillable2,
                    "nillable": True,
                },
            ),
        },
    )
