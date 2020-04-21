from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-ID-enumeration-3-NS"


class NistschemaSvIvAtomicIdEnumeration3Type(Enum):
    """
    :cvar VALUE_WITH_MEASUREMENTS_LACKING_DEGREE_USING_IN_CO:
    :cvar HIN_AND_SOFTWARE_HARDWARE_A:
    :cvar HINTEROPERABILITY_USED_REVOLUTION_METHODS_SYSTEMS_COST_ENA:
    :cvar MTHE_ISSUES_OF_CREATION_BRO:
    :cvar QPRIM:
    :cvar TAND_PERFORMANCE_CAN:
    :cvar USERVICES_ALL_OF:
    :cvar WTO_TO_THE_AND_APPR:
    """
    VALUE_WITH_MEASUREMENTS_LACKING_DEGREE_USING_IN_CO = "_with.measurements.lacking.degree-using_in-co"
    HIN_AND_SOFTWARE_HARDWARE_A = "hin.and-software-hardware-a"
    HINTEROPERABILITY_USED_REVOLUTION_METHODS_SYSTEMS_COST_ENA = "hinteroperability.used.revolution.methods.systems.cost_ena"
    MTHE_ISSUES_OF_CREATION_BRO = "mthe_issues_of_creation-bro"
    QPRIM = "qprim"
    TAND_PERFORMANCE_CAN = "tand-performance-can_"
    USERVICES_ALL_OF = "uservices_all_of_"
    WTO_TO_THE_AND_APPR = "wto-to.the_and.appr"


@dataclass
class Out:
    """
    :ivar any_element:
    """
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class NistschemaSvIvAtomicIdEnumeration3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-ID-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-ID-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicIdEnumeration3Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
