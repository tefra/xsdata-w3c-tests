from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-NCName-minLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 60,
        },
    )
