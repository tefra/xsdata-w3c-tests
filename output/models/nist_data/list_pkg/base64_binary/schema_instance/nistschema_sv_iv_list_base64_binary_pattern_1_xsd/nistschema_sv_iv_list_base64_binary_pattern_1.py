from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-pattern-1-NS"


@dataclass
class NistschemaSvIvListBase64BinaryPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-pattern-1"
        namespace = "NISTSchema-SV-IV-list-base64Binary-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{40} [a-zA-Z0-9+/]{36} [a-zA-Z0-9+/]{12} [a-zA-Z0-9+/]{48} [a-zA-Z0-9+/]{56} [a-zA-Z0-9+/]{60}",
            "tokens": True,
        },
    )
