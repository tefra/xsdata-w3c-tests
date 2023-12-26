from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicShortPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-short-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{5}",
        },
    )
