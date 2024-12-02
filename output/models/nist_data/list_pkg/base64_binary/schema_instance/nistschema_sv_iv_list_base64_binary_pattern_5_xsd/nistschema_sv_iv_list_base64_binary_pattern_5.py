from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-5-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-5"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{36} [a-zA-Z0-9+/]{52} [a-zA-Z0-9+/]{40} [a-zA-Z0-9+/]{56} [a-zA-Z0-9+/]{56} [a-zA-Z0-9+/]{40} [a-zA-Z0-9+/]{56}",
            "tokens": True,
        },
    )
