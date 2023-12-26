from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicTokenPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-token-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){2}Street\s([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s13926-1478",
        },
    )
