from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{20}",
        }
    )
