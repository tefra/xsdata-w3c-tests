from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-length-1-NS"


@dataclass
class NistschemaSvIvListAnyUriLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-length-1"
        namespace = "NISTSchema-SV-IV-list-anyURI-length-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
