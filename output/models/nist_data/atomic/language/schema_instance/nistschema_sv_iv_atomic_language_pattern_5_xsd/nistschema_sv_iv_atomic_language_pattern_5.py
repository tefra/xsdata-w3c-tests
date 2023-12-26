from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicLanguagePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-language-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([a-zA-Z]{2}|[iI]-[a-zA-Z]+|[xX]-[a-zA-Z]{1,8})(-[a-zA-Z]{3})*",
        },
    )
