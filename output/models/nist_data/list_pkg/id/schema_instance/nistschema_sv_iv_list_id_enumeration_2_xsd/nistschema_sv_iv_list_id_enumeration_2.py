from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-ID-enumeration-2-NS"


class NistschemaSvIvListIdEnumeration2Type(Enum):
    ULI_CIS_OF_EMBEDDED_MUST_RECOGNITION_OF_WIDELY_FILES_HAS_ACHALLENGES_THE_IT_FILTER_AND_AS_IN_PROVIDED_BUILD_ACTING_OBJECT_XA_MANIPULATE_WILL_WITH_STAKEHO_FTHE_R_MTRANSACTIONS_MANIPULATE_RELATED_PERVASIVE_FURTHER_FILES_T = (
            "uli",
            "cis-of-embedded-must_recognition.of_widely.files-has",
            "achallenges-the-it_filter.and_as.in.provided-build_acting-object",
            "xa_manipulate_will-with-stakeho",
            "fthe_r",
            "mtransactions.manipulate.related-pervasive.further-files.t",
        )
    HAS_THESE_CHAIN_OBVIOUS_REGISTRY_F_ISOFTWARE_TO_TO_THE_THIS_IN_USE_FOR_OPPORTUNITY_THE_CHAIR_MORE_PARTICULARLY_TRANSMIT_WELL_WAY_TBY_A_TECHNOLOGIES_COMPUTING_RELATED_OF_THE_INFORMATION_REG = (
            "has-these-chain_obvious.registry_f",
            "isoftware-to_to.the_this_in",
            "_use_for.opportunity.the-chair_more",
            "_particularly.transmit-well-way",
            "tby.a.technologies_computing.related_of-the.information-reg",
        )
    SOF_UNDER_COMPLEX_COMPUTING_VLIFE_PART_RINDUSTRIES_HARDWARE_THE_OF_SUCH_NWHICH_GROUPS_USE_TARGETED_INFORMATION_OF_AND_AND_THE_FROM_INVE_BINTEROPERABILITY_TO_DATA_IT_IS_DOCUMENTS_AS_PROMINENT_WMEANS_AND_STRUCTURE_IS_USED_WOULD_SOFTWARE_TO_ISUPP = (
            "sof.under.complex_computing",
            "vlife.part",
            "rindustries.hardware_the-of.such.",
            "nwhich.groups-use.targeted-information.of_and-and-the-from_inve",
            "binteroperability-to_data_it.is_documents_as.prominent_",
            "wmeans",
            "_and-structure_is.used-would-software.to",
            "isupp",
        )
    TECHNOLOGIES_WITH_NPROCESSES_ARE_TO_MA_INFORMATION_AND_D_GLIFE_AND_AN_AND_WORLD_STA_BREGISTRY_MUST_WITHIN_IS_PROCESS_IN_FACIL_GIMAGES_COUPLED_CAN_ASSUR_BA_OTHER_OF_AND_UNDERSTANDING_THE_WITH_REQUIRES_TECHNOLOGI = (
            "_technologies_with_",
            "nprocesses-are-to-ma",
            "_information.and-d",
            "glife.and.an_and-world_sta",
            "bregistry.must_within.is-process.in_facil",
            "gimages.coupled-can_assur",
            "ba_other.of.and_understanding_the.with_requires-technologi",
        )
    NDO_BY_WITH_ELIMINATE_TARGETED_INCLUDING_INTERCONNECTING_OBJECT_DRESPEC_POBJECT_AND_TECHNOLOGY_MUST_AS_MEETS_AND_DATA_THE_OBE_PARTICULARLY_DATABASE_OF_REPRODUCED_WI_SAND_SUBJECT_PROVIDING_FOR_THE_PERFORMANCE_FOR_MEAS_VOF_THESE_AND_GLO_XTH_VTHES_OBY_OF_AND_INTEROPERABILITY_FI = (
            "ndo-by.with-eliminate_targeted-including_interconnecting_object",
            "drespec",
            "pobject.and.technology_must-as_meets.and.data.the",
            "obe-particularly-database_of.reproduced_wi",
            "sand_subject.providing.for.the-performance-for-meas",
            "vof_these_and-glo",
            "xth",
            "vthes",
            "oby-of-and.interoperability_fi",
        )
    EDATA_THE_WIRELESS_CSYS_SUCH_DEFINE_OF_COLLABORATING_VERTIC_HIN_DISCOVERY_AD_THE_ISSUES_INFORMATION_THE_ISSUE_DAPPROACH_PERMITTING_DE_GTWO_CHAIRS_RETRIEVES_OPPORTUNITY_QUALITY_IS_UINDUSTRY_AND_BE_IS_THIS_NEWCO_DAILY_SECURITY_REPOSITORY_MANY_A_GLOBAL_LOC = (
            "edata_the.wireless",
            "csys",
            "_such.define-of.collaborating-vertic",
            "hin.discovery_ad-the-issues_information_the_issue",
            "dapproach.permitting.de",
            "gtwo.chairs-retrieves-opportunity_quality.is.",
            "uindustry-and_be-is-this-newco",
            "_daily.security_repository_many-a_global_loc",
        )
    MSENSORS_GROUPS_MEASURE_FOR_SIMPLEST_FR_NLIBRARIES_THE_COMPUTING_WITH_SECOND_GEN_OBJECTIVE_THE_FOR_BY_LANGUAGE_HAS_THE_CONFERENCES_IS_IN_QLOCATION_THE_QU_CASSURING_IS_INDUSTRY_UTILITI_VON_OUR_AN_VERSIONS_OF_RETRIEVE_INFOR_TON_SYSTEMS_ASSURING_DOCUMENTS_PROCES_JFOR_SIGNIFICANT_DISCOVER_EFFECTIVE_REGISTRY_AS_DIVISIONS_AND_CR = (
            "msensors-groups-measure_for_simplest_fr",
            "nlibraries_the_computing.with-second-gen",
            "_objective.the-for_by-language_has.the_conferences.is-in",
            "qlocation.the.qu",
            "cassuring_is.industry.utiliti",
            "von-our-an.versions.of-retrieve-infor",
            "ton-systems.assuring_documents-proces",
            "jfor_significant_discover.effective.registry.as_divisions-and",
            "cr",
        )
    THAT_SPECIFICATIONS_TO_USED_INFORMAT_THAT_THE_FOR_REGISTRY_WIDE_QAROUND_THESE_THE_ASKED_TO_PROGRAM_MANIPULATION_AN_A_ACAD_STANDARDS_THIS_MUS_CCONTRIBUTE_DEFINES_CON_SLAW_BE = (
            "_that.specifications-to.used-informat",
            "_that.the_for_registry_wide_",
            "qaround.these_the_asked.to.program.manipulation_an.a-acad",
            "_standards-this_mus",
            "ccontribute-defines.con",
            "slaw-be",
        )


@dataclass
class Out:
    class Meta:
        name = "out"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-2-NS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class NistschemaSvIvListIdEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-ID-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-ID-enumeration-2-NS"

    value: Optional[NistschemaSvIvListIdEnumeration2Type] = field(
        default=None
    )
