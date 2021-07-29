from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicStringPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-string-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\n([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s17687",
        }
    )
