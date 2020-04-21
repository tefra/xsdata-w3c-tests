from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-1-NS"


class NistschemaSvIvAtomicNameEnumeration1Type(Enum):
    """
    :cvar AND_A_INCLUDING_AS_THE_COUPLED_IN_COMPLEX_THIS_AT_AND_A_I:
    :cvar PROCESSES_AND_BOTH_FI:
    :cvar VALUE_PARTICULAR_AS_PARTICIPANTS_STANDARDIZATION_DAT:
    :cvar AIS_PROFILES_ACADEMIA_FOR_BE:
    :cvar LSOFTWARE_QUALITY_AND_INTEROPERABILITY_IN_COMMERCE_TEST_WILL_G:
    :cvar OAND_LEADERSHIP_THE_AS_MANUFACTURERS_TH:
    :cvar RTHE_ENABLING_SET_FROM_D:
    :cvar TPRIMARY_NEED_THE_DOCUMENTS_MAINTAI:
    """
    AND_A_INCLUDING_AS_THE_COUPLED_IN_COMPLEX_THIS_AT_AND_A_I = ":and-a:including_as.the-coupled.in.complex:this-at:and.a_i"
    PROCESSES_AND_BOTH_FI = ":processes_and.both.fi"
    VALUE_PARTICULAR_AS_PARTICIPANTS_STANDARDIZATION_DAT = "_particular:as_participants:standardization.dat"
    AIS_PROFILES_ACADEMIA_FOR_BE = "ais_profiles:academia:for-be"
    LSOFTWARE_QUALITY_AND_INTEROPERABILITY_IN_COMMERCE_TEST_WILL_G = "lsoftware-quality_and:interoperability:in-commerce-test:will:.g"
    OAND_LEADERSHIP_THE_AS_MANUFACTURERS_TH = "oand.leadership_the.as-manufacturers_th"
    RTHE_ENABLING_SET_FROM_D = "rthe:enabling-set_from:d"
    TPRIMARY_NEED_THE_DOCUMENTS_MAINTAI = "tprimary-need:the:documents_maintai"


@dataclass
class NistschemaSvIvAtomicNameEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-1-NS"

    value: Optional[NistschemaSvIvAtomicNameEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
