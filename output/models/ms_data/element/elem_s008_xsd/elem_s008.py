from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xsdtesting"


@dataclass(kw_only=True)
class CInvalid:
    class Meta:
        name = "c_invalid"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Cs:
    class Meta:
        name = "cs"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 4,
        },
    )
    a: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Cc(Cs):
    class Meta:
        name = "cc"

    b: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FrValid(Cs):
    class Meta:
        name = "fr_valid"
        namespace = "http://xsdtesting"


@dataclass(kw_only=True)
class Fr1Valid(Cc):
    class Meta:
        name = "fr1_valid"
        namespace = "http://xsdtesting"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fr1_valid_or_fr_valid: None | Fr1Valid | FrValid = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "fr1_valid",
                    "type": Fr1Valid,
                },
                {
                    "name": "fr_valid",
                    "type": FrValid,
                },
            ),
        },
    )
