from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-length-5-NS"


@dataclass
class NistschemaSvIvListAnyUriLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-length-5"
        namespace = "NISTSchema-SV-IV-list-anyURI-length-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
