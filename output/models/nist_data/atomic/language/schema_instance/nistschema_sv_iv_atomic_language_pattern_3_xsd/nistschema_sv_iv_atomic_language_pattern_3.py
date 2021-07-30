from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicLanguagePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-language-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([a-zA-Z]{2}|[iI]-[a-zA-Z]+|[xX]-[a-zA-Z]{1,8})(-[a-zA-Z]{3})*",
        }
    )
