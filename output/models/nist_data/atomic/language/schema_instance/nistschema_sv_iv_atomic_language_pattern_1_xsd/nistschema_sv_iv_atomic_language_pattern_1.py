from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicLanguagePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-language-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([a-zA-Z]{2}|[iI]-[a-zA-Z]+|[xX]-[a-zA-Z]{1,8})(-[a-zA-Z]{3})*",
        },
    )
