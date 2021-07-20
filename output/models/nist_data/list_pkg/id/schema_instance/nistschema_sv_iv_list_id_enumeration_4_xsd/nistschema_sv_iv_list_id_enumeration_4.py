from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-enumeration-4-NS"


class NistschemaSvIvListIdEnumeration4Type(Enum):
    CINTUITIVE_RETRIEVE_PARTNERS_BY_THE_UNBIASED_WORLD_SUPPORT_MLIBRARIES_ADDRESSING_TECHNICAL_BUILDING_WITH_OF_AREAS_REPO_DS_ILEADERSHIP_A_VARIETY_MOST_AT_IS_A_DONATE_BE_MA_KNETWORKING_MANY_THE_DATA_MANY_HAS_PROMINENT_FOR_LAW_PROV = (
            "cintuitive.retrieve.partners_by_the-unbiased.world-support",
            "mlibraries_addressing-technical_building.with-of.areas-repo",
            "ds",
            "ileadership.a.variety.most-at-is-a_",
            "_donate_be.ma",
            "knetworking.many_the.data.many_has-prominent_for.law.prov",
        )
    RINTERNATIONAL_SOFTWARE_WHERE_GREAT_AND_INTERACTIN_WI_WAND_AND_THE_AND_S_FOR_REPO_LOOKI_CTEST_RECOMMENDING_ISSUES_COMPUTED_AS_INCLUDING = (
            "rinternational_software_where_great_and-interactin",
            "_wi",
            "wand.and-the_and_s-for_repo",
            "_looki",
            "ctest.recommending_issues-computed.as-including",
        )
    HWITH_INFORMATION_TO_AP_TECHNOLOGIES_LANGUAGES_AND_THESE_AND_SOFTWARE_AND_ALS_TT_OLOW_COST_THAT_TOOLS_EXCHANGE_PERVASIVE_OF_TOOLS_OF_D_CA_INDUSTRY_DISCOVERY_UNBIASED_DO_MTHE_COMPATIBILITY_LAN_JRESPECT_LIFE_ENGINEERING_WITH_A_AND_HDYNAMIC_ALSO_DRAFT_TECHNICAL_RELATED = (
            "hwith.information_to_ap",
            "_technologies.languages-and-these-and-software.and_als",
            "tt",
            "olow-cost-that.tools-exchange.pervasive_of-tools_of-d",
            "ca-industry.discovery.unbiased_do",
            "mthe-compatibility.lan",
            "jrespect-life-engineering-with_a_and_",
            "hdynamic_also.draft.technical_related.",
        )
    SSPE_KSIGNATURES_DEFINES_FURTHER_CONFERENCES_PORTABLE_IS_ELECT_XREFERENCE_CHAIN_AND_MANAGEMENT_PORTABLE_KEY_AND_E_AND_CAPABILITIES_STANDARDS_WORK_LIES_REGISTRY_TO_THE_PINDUSTRY_AND_IMPACT_PRIMAR_NCHALLENGES_AND_THESE_A_TO_THE_AND_OF_ENSURE_TRANSMIT_ADDRES_XOBJECT_MORE_AND_PROCESSES_BE_IN = (
            "sspe",
            "ksignatures_defines.further_conferences_portable-is.elect",
            "xreference-chain-and.management_portable_key.and-",
            "_e_and-capabilities-standards.work.lies.registry.to_the-",
            "pindustry-and_impact.primar",
            "nchallenges.and_these.a-to_the_and-of.ensure_transmit.addres",
            "xobject-more-and-processes.be.in",
        )
    THE_MEDIUM_SIZED_JAND_G_TOOL_LIBRARIES_MATCH_NEEDED_PARTICIPATE_MANUAL_AND_ALL_R_GSPECIFICATIONS_OF_USE_FOR_COMPUTIN_ECRITERIA_COF_OBJECT_AUTOMATIC_ISSUES_A_ADDITIONALLY_COMPUTER_SI_THE_OR_FORMED_FOR_MULTIDISCIPLINARY_NEW_BASE_THE_B_CAND_TUNE_SYSTEMS_ON_A_CHIP_THE_AS_MANIPULATION_DEPLOYED_OF = (
            "_the_medium-sized_",
            "jand.",
            "_g.tool_libraries-match.needed.participate_manual-and-all_r",
            "gspecifications.of.use-for-computin",
            "ecriteria",
            "cof.object-automatic.issues.a_additionally-computer-si",
            "_the_or.formed-for_multidisciplinary-new.",
            "_base_the-b",
            "cand_tune-systems-on-a-chip_the.as.manipulation.deployed_of",
        )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-4-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvListIdEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-4-NS"

    value: Optional[NistschemaSvIvListIdEnumeration4Type] = field(
        default=None
    )
