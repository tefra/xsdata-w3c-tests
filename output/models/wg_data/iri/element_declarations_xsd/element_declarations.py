from dataclasses import dataclass, field


@dataclass
class Iri3987:
    class Meta:
        name = "IRI-3987"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class IriReference3987:
    class Meta:
        name = "IRI-reference-3987"

    value: str = field(
        default="",
        metadata={
            "pattern": r"",
        }
    )


@dataclass
class Uri3986:
    class Meta:
        name = "URI-3986"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class UriReference3986:
    class Meta:
        name = "URI-reference-3986"

    value: str = field(
        default="",
        metadata={
            "pattern": r"",
        }
    )


@dataclass
class AbsoluteIri3987:
    class Meta:
        name = "absolute-IRI-3987"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class AbsoluteUri3986:
    class Meta:
        name = "absolute-URI-3986"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class RelativeReference3986:
    class Meta:
        name = "relative-reference-3986"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )


@dataclass
class RelativeReference3987:
    class Meta:
        name = "relative-reference-3987"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"",
        }
    )
