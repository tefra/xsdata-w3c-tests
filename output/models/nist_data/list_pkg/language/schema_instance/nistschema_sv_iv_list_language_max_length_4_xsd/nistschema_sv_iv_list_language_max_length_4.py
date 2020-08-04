from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-maxLength-4-NS"


@dataclass
class NistschemaSvIvListLanguageMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-language-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-language-maxLength-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=8,
            tokens=True
        )
    )
