from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-length-2-NS"


@dataclass
class NistschemaSvIvListLanguageLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-length-2"
        namespace = "NISTSchema-SV-IV-list-language-length-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 6,
            "tokens": True,
        },
    )
