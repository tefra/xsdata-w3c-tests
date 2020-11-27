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
            "required": True,
        }
    )


@dataclass
class Cs:
    class Meta:
        name = "cs"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "max_length": 2,
        }
    )
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Fe1Valid:
    class Meta:
        name = "fe1_valid"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )


@dataclass
class FeValid:
    class Meta:
        name = "fe_valid"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 4,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fe1_valid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 2,
        }
    )
    fe_valid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 4,
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
