from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-enumeration-3-NS"


class NistschemaSvIvListIdEnumeration3Type(Enum):
    MLEADERS_FFACT_PRODUC_FAND_MEMORY_THAT_AND_MEA_ACHIEVED_SIGNATURE_P_TCOMPATIBILITY_TO_ABOUT_NETWORKING_ROBUST_FROM_FOR_TH_XWHICH_OF_BUSINESS_INCLUDE_THESE_DEVICES_THE = "mleaders ffact_produc fand-memory_that-and.mea _achieved_signature-p tcompatibility_to_about-networking-robust-from_for_th xwhich-of-business_include.these_devices_the"
    VA_OF_USERS_THE_AND_AN_TO_FOR_VOICED_PROFILE_OF_XTHE_POSSIBLE_SUCCESS_WEB_OF_INCLUDING_I_YWIDE_DEFINES_BUS_AND_SMALL_BOTTLENECKS_THE_FIL_DOF_THE_TO_WID_LED_LOCALIZED_THE_TRANSFORMING_REGISTRIES_BY_OTO_INFORMATION_G_SENSORS_A_OLDER_OVER_INDUSTRY_PROVIDE_ENOUGH_INFLUENCE_NEWCOM = "va-of-users-the.and.an_to-for-voiced.profile-of_ xthe.possible.success.web.of_including_i ywide_defines.bus _and.small-_bottlenecks.the_fil dof.the-to_wid _led-localized_the.transforming_registries_by- oto-information-g_sensors.a.older.over.industry.provide-enough- _influence_newcom"
    TREPOSITORY_AN_C_ICOMPUTING_FOR_AS_TESTING_MAKE_SOFTWARE_OF_INTERNATIONAL_NRETRIEVE_SENSE_TO_THEIR_SOL_XAPPLICATIONS_OF_AND_THE_FRAMEWORKS_THE_SPECIFIC_S_THESE_WE_RET_TSECOND_GENERATION_HAS_TO_LARGE_THE_THEM_RELAT_BCAN_MUST_CCOMPATIBILITY_SHIFT_G_AS_PARTNER_TKNOWN_FOR_WITH_SYSTEM_AREAS_CHO = "trepository_an.c icomputing_for-as.testing_make.software_of-international nretrieve-sense-to_their_sol xapplications-of.and_the-frameworks_the-specific-s.these_we-ret tsecond-generation.has-to.large.the_them.relat bcan-must ccompatibility_shift.g.as.partner tknown_for.with.system-areas.cho"
    LSPECIFICATIONS_TOOL_NEW_WIRELESS_THE_ARE_H_CCONSISTENCY_TO_PERSONAL_RBACK_IN_OF_THE_ON_AS_PROTOTYPE_PROVIDES_IN_LED_THE_PROVIDE_HUSER_ALL_TECHNOLOGY_THE_MUST_AS_BE_PROFILE_FOR_COMPETEN_XSTRUCTURE_USES_CUSED_AND_OF_IS_COMPUTING_ASPECTS_THOSE_E_NAND_BE_REPOSITORY_TESTS_ITS_CTHE_STAKEHOLDERS_DIRECTIONS_DEFINE_OF_BECOME_SOFTWA = "lspecifications-tool_new.wireless.the.are.h cconsistency.to-personal rback_in-of_the-on.as-prototype-provides-in_led-the-provide huser-all.technology-the_must_as-be.profile_for-competen xstructure-uses cused_and_of.is.computing.aspects.those.e nand-be_repository_tests.its cthe-stakeholders.directions.define-of_become_softwa"
    BRIGOROUS_THAT_CAN_TO_CRE_CCOST_OF_MANIPULATE_SEN_KINVOLVED_ORGANIZATIONS_AND_ISSUES_UWELL_DEVICES_HAS_WITH_BENEFITS_AUTOMATIC_MOST_STA_AND_SPECIFICATIONS_INDIVIDUAL_PORTABLE_SERIES_USE_QAND_THE_COME_THE_FILE_AU = "brigorous.that-can.to_cre ccost.of_manipulate_sen kinvolved.organizations-and.issues uwell-devices.has-with-benefits_automatic.most_sta _and_specifications.individual.portable_series.use qand-the_come-the.file_au"
    PLED_AND_THESE_AMONG_REPUTATION_FULL_AN_RECOGNITION_AND_INDICATION_UNDERSTAND_INDUSTRY_APPL_YAN_VCREATION_MEANS_TOOLS_ON_WITH_IS_THE_FIVE_WILL_H_NUNBIASED_RESULT_FROM_OUR_GENERATION_FILES_ALLOW_R_QBOTH_COMPLETION_PROCESSORS_RI_CF_QTO_EMBEDDED_ANY_EFFECTIVELY_AREAS_OF = "pled_and_these.among-reputation.full_an _recognition_and-indication.understand-industry-appl yan vcreation_means_tools_on.with_is.the_five_will_h nunbiased-result_from.our.generation-files_allow-r qboth-completion_processors-ri cf qto-embedded.any_effectively_areas_of."
    MGUIDELINES_FOR_CHOICES_MARKET_MANIP_URETRIEVES_THE_WILL_OF_COST_FR_PL_PBETWEEN_TO_ENFORCEM_VFOR_HELP_WITH_AND_PRECISE_DEVELOPED_THAT_IN_USED_REVIE = "mguidelines-for.choices.market.manip uretrieves.the.will_of_cost-fr pl pbetween-to.enforcem vfor.help.with.and-precise-developed-that_in_used.revie"


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-3-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvListIdEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-3-NS"

    value: Optional[NistschemaSvIvListIdEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
