from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-language-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicLanguagePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-language-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-language-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"([a-zA-Z]{2}|[iI]-[a-zA-Z]+|[xX]-[a-zA-Z]{1,8})(-[a-zA-Z]{3})*",
        }
    )
