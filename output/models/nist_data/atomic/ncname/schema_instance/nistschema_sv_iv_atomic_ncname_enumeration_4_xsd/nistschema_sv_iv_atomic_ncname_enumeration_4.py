from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-enumeration-4-NS"


class NistschemaSvIvAtomicNcnameEnumeration4Type(Enum):
    XSTANDARDS_AND_ALL_DIFFERENT_SUCH_THE_PARTICULARLY_TRANSMIT_TO = "xstandards-and-all-different-such.the_particularly.transmit_to"
    KINDICATION_ALL_A_OF_RESOURCES_WITH_COST_VIA = "kindication.all-a_of_resources_with.cost-via-"
    WELECTRONIC_WORKI = "welectronic-worki"
    IOF_FOR_IN_IN_REPOSITORY_OTHER_AND_OF_I = "iof_for-in.in-repository_other.and-of-i"
    WITHIN_CAN_STANDARD_AND_FO = "_within.can.standard-and_fo"
    NTO_USE = "nto-use"
    OEXECUTION_INDUSTRY_DATA_INDUS = "oexecution_industry_data_indus"
    WUPON_AND_AVAILABLE_AND_IS_TO_AMONG_AND_APPLICATION = "wupon-and_available.and-is.to.among_and_application-"


@dataclass
class NistschemaSvIvAtomicNcnameEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-NCName-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicNcnameEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
