from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-NCName-minLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 64,
        },
    )
