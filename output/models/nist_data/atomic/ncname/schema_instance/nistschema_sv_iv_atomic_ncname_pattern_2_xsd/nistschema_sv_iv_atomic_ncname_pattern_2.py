from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicNcnamePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-NCName-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[\i-[:]][\c-[:]]{40}",
        }
    )
