from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-pattern-5-NS"


@dataclass
class NistschemaSvIvListNamePattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-pattern-5"
        namespace = "NISTSchema-SV-IV-list-Name-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\i\c{21} \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33} \i\c{44} \i\c{57}",
            tokens=True
        )
    )
