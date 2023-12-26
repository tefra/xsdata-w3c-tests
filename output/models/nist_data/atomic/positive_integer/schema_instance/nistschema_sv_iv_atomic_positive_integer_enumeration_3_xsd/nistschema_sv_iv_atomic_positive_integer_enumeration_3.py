from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-3-NS"


class NistschemaSvIvAtomicPositiveIntegerEnumeration3Type(Enum):
    VALUE_12730 = 12730
    VALUE_518340460 = 518340460
    VALUE_27263821738066862 = 27263821738066862
    VALUE_63621988 = 63621988
    VALUE_7678 = 7678
    VALUE_7942666042 = 7942666042


@dataclass
class NistschemaSvIvAtomicPositiveIntegerEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-enumeration-3-NS"

    value: Optional[
        NistschemaSvIvAtomicPositiveIntegerEnumeration3Type
    ] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
