from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-list-language-enumeration-4-NS"


class NistschemaSvIvListLanguageEnumeration4Type(Enum):
    HA_HI_HR_HU_HY_IA_IE_IK = (
        "HA",
        "HI",
        "HR",
        "HU",
        "HY",
        "IA",
        "IE",
        "IK",
    )
    BG_BH_BI_BN_BO_BR_CA = (
        "BG",
        "BH",
        "BI",
        "BN",
        "BO",
        "BR",
        "CA",
    )
    SS_ST_SU_SV_SW = (
        "SS",
        "ST",
        "SU",
        "SV",
        "SW",
    )
    MR_MS_MT_MY_NA_NE_NL_NO_OC = (
        "MR",
        "MS",
        "MT",
        "MY",
        "NA",
        "NE",
        "NL",
        "NO",
        "OC",
    )
    RN_RO_RU_RW_SA_SD_SG_SH_SI = (
        "RN",
        "RO",
        "RU",
        "RW",
        "SA",
        "SD",
        "SG",
        "SH",
        "SI",
    )
    ES_ET_EU_FA_FI = (
        "ES",
        "ET",
        "EU",
        "FA",
        "FI",
    )
    IS_IT_IW_JA_JI = (
        "IS",
        "IT",
        "IW",
        "JA",
        "JI",
    )
    HR_HU_HY_IA_IE_IK = (
        "HR",
        "HU",
        "HY",
        "IA",
        "IE",
        "IK",
    )


@dataclass(kw_only=True)
class NistschemaSvIvListLanguageEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-language-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-language-enumeration-4-NS"

    value: NistschemaSvIvListLanguageEnumeration4Type = field(
        metadata={
            "required": True,
        }
    )
