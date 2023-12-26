from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicLanguageMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-language-minLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
        },
    )
