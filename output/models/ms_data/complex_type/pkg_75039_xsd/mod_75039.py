from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Complex11:
    """
    :ivar any_element:
    """
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
    """This is defined to be of type 'xsd:anyType'.

    :ivar any_element:
    """
    class Meta:
        name = "substHead"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
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
    """
    :ivar complex2:
    :ivar complex1:
    :ivar subst_head:
    """
    class Meta:
        name = "bagOfHeads"

    complex2: List[Complex2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex1: List[Complex1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    subst_head: List[SubstHead] = field(
        default_factory=list,
        metadata={
            "name": "substHead",
            "type": "Element",
        }
    )
