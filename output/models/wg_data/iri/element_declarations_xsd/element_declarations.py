from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Iri3987:
    class Meta:
        name = "IRI-3987"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class IriReference3987:
    class Meta:
        name = "IRI-reference-3987"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"",
        }
    )


@dataclass
class Uri3986:
    class Meta:
        name = "URI-3986"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"((([A-Za-z])[A-Za-z0-9+\-\.]*):((\?((([A-Za-z0-9\-\._~!$&'()*+,;=:@]|(%[0-9A-Fa-f][0-9A-Fa-f]))|/|\?))*))?((#((([A-Za-z0-9\-\._~!$&'()*+,;=:@]|(%[0-9A-Fa-f][0-9A-Fa-f]))|/|\?))*))?)",
        }
    )


@dataclass
class UriReference3986:
    class Meta:
        name = "URI-reference-3986"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"((([A-Za-z])[A-Za-z0-9+\-\.]*):((\?((([A-Za-z0-9\-\._~!$&'()*+,;=:@]|(%[0-9A-Fa-f][0-9A-Fa-f]))|/|\?))*))?((#((([A-Za-z0-9\-\._~!$&'()*+,;=:@]|(%[0-9A-Fa-f][0-9A-Fa-f]))|/|\?))*))?)",
        }
    )


@dataclass
class AbsoluteIri3987:
    class Meta:
        name = "absolute-IRI-3987"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class AbsoluteUri3986:
    class Meta:
        name = "absolute-URI-3986"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"((([A-Za-z])[A-Za-z0-9+\-\.]*):((\?((([A-Za-z0-9\-\._~!$&'()*+,;=:@]|(%[0-9A-Fa-f][0-9A-Fa-f]))|/|\?))*))?)",
        }
    )


@dataclass
class RelativeReference3986:
    class Meta:
        name = "relative-reference-3986"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class RelativeReference3987:
    class Meta:
        name = "relative-reference-3987"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"",
        }
    )
