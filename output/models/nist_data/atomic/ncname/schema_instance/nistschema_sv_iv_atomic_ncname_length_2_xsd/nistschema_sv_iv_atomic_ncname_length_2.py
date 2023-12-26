from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-length-2-NS"


@dataclass
class NistschemaSvIvAtomicNcnameLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-length-2"
        namespace = "NISTSchema-SV-IV-atomic-NCName-length-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 61,
        },
    )
