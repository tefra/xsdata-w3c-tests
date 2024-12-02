from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-maxLength-2-NS"


@dataclass
class NistschemaSvIvListLanguageMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-language-maxLength-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
