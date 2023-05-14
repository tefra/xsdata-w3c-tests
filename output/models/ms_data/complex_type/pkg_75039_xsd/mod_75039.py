from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Complex11:
    class Meta:
        name = "COMPLEX1"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Complex21:
    class Meta:
        name = "COMPLEX2"


@dataclass
class SubstHead:
    """
    This is defined to be of type 'xsd:anyType'.
    """
    class Meta:
        name = "substHead"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Complex1(Complex11):
    class Meta:
        name = "complex1"


@dataclass
class Complex2(Complex21):
    class Meta:
        name = "complex2"


@dataclass
class BagOfHeads:
    class Meta:
        name = "bagOfHeads"

    complex2_or_complex1_or_subst_head: List[object] = field(
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
        }
    )
