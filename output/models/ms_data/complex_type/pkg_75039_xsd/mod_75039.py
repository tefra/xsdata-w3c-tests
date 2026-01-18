from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Complex11:
    class Meta:
        name = "COMPLEX1"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Complex21:
    class Meta:
        name = "COMPLEX2"


@dataclass(kw_only=True)
class SubstHead:
    """
    This is defined to be of type 'xsd:anyType'.
    """

    class Meta:
        name = "substHead"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Complex1(Complex11):
    class Meta:
        name = "complex1"


@dataclass(kw_only=True)
class Complex2(Complex21):
    class Meta:
        name = "complex2"


@dataclass(kw_only=True)
class BagOfHeads:
    class Meta:
        name = "bagOfHeads"

    complex2_or_complex1_or_subst_head: list[
        Complex2 | Complex1 | SubstHead
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "complex2",
                    "type": Complex2,
                },
                {
                    "name": "complex1",
                    "type": Complex1,
                },
                {
                    "name": "substHead",
                    "type": SubstHead,
                },
            ),
        },
    )
