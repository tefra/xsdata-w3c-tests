from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-NCName-pattern-2-NS"


@dataclass
class NistschemaSvIvListNcnamePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-NCName-pattern-2"
        namespace = "NISTSchema-SV-IV-list-NCName-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46} [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58} [\i-[:]][\c-[:]]{11}",
            "tokens": True,
        },
    )
