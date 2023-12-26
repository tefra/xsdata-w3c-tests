from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicStringPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-string-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){2}Street\n([A-Z][a-z]{1,20}\s){3},\s[A-Z]{2}\s15849",
        },
    )
