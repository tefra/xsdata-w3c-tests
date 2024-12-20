from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-3-NS"


@dataclass
class NistschemaSvIvListNcnamePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-3"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}",
            "tokens": True,
        },
    )
