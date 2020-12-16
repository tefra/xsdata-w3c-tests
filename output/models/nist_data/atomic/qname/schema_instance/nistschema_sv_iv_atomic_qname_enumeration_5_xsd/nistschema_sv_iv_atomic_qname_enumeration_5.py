from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"


class NistschemaSvIvAtomicQnameEnumeration5Type(Enum):
    UTHE_BASE_THE_ABILITY_INTO_TARGET_THE_TESTABILITY_DISCOVE = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-5-NS}uthe.base_the_ability-into-target_the_testability-discove")
    FOR_FILES_SUPPLY_FOR_TO_MUST_MEASUR = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-5-NS}_for-files.supply.for.to-must_measur")
    D_I = QName("{http://www.nist.gov/xsdNS}i")
    PS_PERVASIVE_IN_HOUSE_ON_PERFORMANCE_ALS = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-5-NS}ps.pervasive.in-house_on.performance-als")
    BUILD_RETRIEVES_COR_AMONG_TO_MUST_AND_INDUSTRY_FROM_THAT = QName("{http://www.nist.gov/xsdNS}_among.to.must_and.industry-from-that_")
    HMANIPULATE_US = QName("{NISTSchema-SV-IV-atomic-QName-enumeration-5-NS}hmanipulate-us")


@dataclass
class ForFilesSupplyForToMustMeasur:
    class Meta:
        name = "_for-files.supply.for.to-must_measur"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class HmanipulateUs:
    class Meta:
        name = "hmanipulate-us"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PsPervasiveInHouseOnPerformanceAls:
    class Meta:
        name = "ps.pervasive.in-house_on.performance-als"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class UtheBaseTheAbilityIntoTargetTheTestabilityDiscove:
    class Meta:
        name = "uthe.base_the_ability-into-target_the_testability-discove"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvAtomicQnameEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-QName-enumeration-5-NS"

    value: Optional[NistschemaSvIvAtomicQnameEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
