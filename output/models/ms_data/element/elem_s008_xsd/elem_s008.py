from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class CInvalid:
    class Meta:
        name = "c_invalid"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Cs:
    class Meta:
        name = "cs"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 4,
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Cc(Cs):
    class Meta:
        name = "cc"

    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FrValid(Cs):
    class Meta:
        name = "fr_valid"
        namespace = "http://xsdtesting"


@dataclass
class Fr1Valid(Cc):
    class Meta:
        name = "fr1_valid"
        namespace = "http://xsdtesting"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fr1_valid: Optional[Fr1Valid] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fr_valid: Optional[FrValid] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
