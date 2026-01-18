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
            "required": True,
            "min_length": 1,
            "max_length": 2,
        },
    )
    a: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Fe1Valid:
    class Meta:
        name = "fe1_valid"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 2,
        },
    )


@dataclass(kw_only=True)
class FeValid:
    class Meta:
        name = "fe_valid"
        namespace = "http://xsdtesting"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 4,
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
class Root:
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fe1_valid_or_fe_valid: None | Fe1Valid | FeValid = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "fe1_valid",
                    "type": Fe1Valid,
                },
                {
                    "name": "fe_valid",
                    "type": FeValid,
                },
            ),
        },
    )
