from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-length-1-NS"


@dataclass
class NistschemaSvIvAtomicNcnameLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-length-1"
        namespace = "NISTSchema-SV-IV-atomic-NCName-length-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 1,
        },
    )
