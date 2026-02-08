from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-enumeration-1-NS"


class NistschemaSvIvAtomicNameEnumeration1Type(Enum):
    PARTICULAR_AS_PARTICIPANTS_STANDARDIZATION_DAT = (
        "_particular:as_participants:standardization.dat"
    )
    LSOFTWARE_QUALITY_AND_INTEROPERABILITY_IN_COMMERCE_TEST_WILL_G = (
        "lsoftware-quality_and:interoperability:in-commerce-test:will:.g"
    )
    RTHE_ENABLING_SET_FROM_D = "rthe:enabling-set_from:d"
    TPRIMARY_NEED_THE_DOCUMENTS_MAINTAI = "tprimary-need:the:documents_maintai"
    PROCESSES_AND_BOTH_FI = ":processes_and.both.fi"
    AIS_PROFILES_ACADEMIA_FOR_BE = "ais_profiles:academia:for-be"
    AND_A_INCLUDING_AS_THE_COUPLED_IN_COMPLEX_THIS_AT_AND_A_I = (
        ":and-a:including_as.the-coupled.in.complex:this-at:and.a_i"
    )
    OAND_LEADERSHIP_THE_AS_MANUFACTURERS_TH = (
        "oand.leadership_the.as-manufacturers_th"
    )


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNameEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-Name-enumeration-1-NS"

    value: NistschemaSvIvAtomicNameEnumeration1Type = field()
