from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-minLength-4-NS"


@dataclass
class NistschemaSvIvListLanguageMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-minLength-4"
        namespace = "NISTSchema-SV-IV-list-language-minLength-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
