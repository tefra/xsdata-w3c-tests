from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"


class NistschemaSvIvListQnameEnumeration4Type(Enum):
    """
    :cvar DATA_COMM_OAND_TO_AS_AND_S_EACH_DO_REPOSITORY_SPE_KRELATED_DISCOVERY_CONFOR_RDI_THE_IIS_DESKTOP_INFORMATION_IN_FILTE_YPROFILES_SPECIFICATIONS_IS_ASS_IPROC_XFILE_AND:
    :cvar IPROC_XFILE_AND_HAMPERED_ON_HAS_BACK_MEASURE_AND_BROWSERS_INVESTIGATIO_OENABLE_OIS_GLOBAL_T_ALL_THEM_SEMANTICS_AND_TOOL_REFERENCE_AND_THE_INCLUDE_IMPROVE_AND_ADDRESSING_PARTNERSHIPS_A_AND_DATA_TOOL_SPECIFICATION_CALLED_CORRECTIO:
    :cvar ROF_IPROVIDES_THE_MADE_VOI_INTEROPERABILITY_LA_RSERVICE_COMPUTER_SHIFT_OF_MUST_IN_LIES_THE_REQUESTING_STRUCTURE_SYST_KSUPPLY_OFFER_S_USING_YEA_XCOMPETENCE_BUSINESS_AND_IS_DYN_V_G20_SOFTWARE_SP:
    :cvar SERIE_YAN_SIMULATION_SUCH_BACK_EACH_MAN_WITH_VCOMPUTING_THE_OF_BUILDING_KEY_MAINTAINS_ADVANCED_THE_STAKEHOL_NOF_FOUR_INFORMATION_TO_SSIGNATURES_SET_FILE_AND_OBJECT_THE_IS_INFORMATION_THE_MENVIRONMENT_FOR_SUPPLY_OF_DEVEL_QALSO_CORRECTION_IN_CONTEXT_RICH_AND_IS_D_EPROVIDED_TO_PADVENT_ITS_TESTABLE_THEM_BANDWIDTH_MO_VAND_CONSOR_DATA_COMM_OAND_TO_AS_AND_S:
    :cvar V_G20_SOFTWARE_SP_NO_COMPUTING_CASKING_FOR_IMPL_UAREA_FAN_ARE_TEST_FRAMEWORKS_TECHNICAL_WIREL_YC_VBUILDING_THE_TO_CONTEXT_R:
    :cvar YC_VBUILDING_THE_TO_CONTEXT_R_ACARE_FILE_SECURITY_FILE_AREA_SOF_AS_AND_THE_INDUSTRY_SOFTWARE_AND_THE_NETWORKS_COMPETENCE_EWITH_TE_JTO_NEUTRAL_TEC_CONTAINING_USED_VISIBLY_TEST_CONSORTIUMS_THIS_SECURITY_PROF_DBASIS_AND_CONTAINS_THAT_AND_2000_PARADIGM_REVOLUTION_DES_XTHE_PERVASIVE_AUTOM_AMONG_WHICH_TO_OF_TE_AMBIGUITIES_DHELPING_HAVE_AND_VOCABU_SERIE_YAN_SIMULATION_SUCH_BACK_EACH_MAN:
    """
    DATA_COMM_OAND_TO_AS_AND_S_EACH_DO_REPOSITORY_SPE_KRELATED_DISCOVERY_CONFOR_RDI_THE_IIS_DESKTOP_INFORMATION_IN_FILTE_YPROFILES_SPECIFICATIONS_IS_ASS_IPROC_XFILE_AND = "_data.comm:oand-to.as_and-s _each_do-repository.spe:krelated_discovery.confor rdi:_the. iis_desktop_information_in _filte:yprofiles_specifications.is_ass iproc:xfile-and_"
    IPROC_XFILE_AND_HAMPERED_ON_HAS_BACK_MEASURE_AND_BROWSERS_INVESTIGATIO_OENABLE_OIS_GLOBAL_T_ALL_THEM_SEMANTICS_AND_TOOL_REFERENCE_AND_THE_INCLUDE_IMPROVE_AND_ADDRESSING_PARTNERSHIPS_A_AND_DATA_TOOL_SPECIFICATION_CALLED_CORRECTIO = "iproc:xfile-and_ _hampered_on_has-back_measure_and_browsers-investigatio oenable_:ois_global-t _all-them-semantics.and_tool-reference.and.the_include-improve _and-addressing_partnerships.a_and_data_tool _specification_called.correctio"
    ROF_IPROVIDES_THE_MADE_VOI_INTEROPERABILITY_LA_RSERVICE_COMPUTER_SHIFT_OF_MUST_IN_LIES_THE_REQUESTING_STRUCTURE_SYST_KSUPPLY_OFFER_S_USING_YEA_XCOMPETENCE_BUSINESS_AND_IS_DYN_V_G20_SOFTWARE_SP = "rof:iprovides_the_made_voi _interoperability.la:rservice-computer-shift. _of_must_in.lies.the.requesting-structure-syst ksupply-offer.s-using.yea xcompetence.business_and.is_dyn v:g20-software_sp"
    SERIE_YAN_SIMULATION_SUCH_BACK_EACH_MAN_WITH_VCOMPUTING_THE_OF_BUILDING_KEY_MAINTAINS_ADVANCED_THE_STAKEHOL_NOF_FOUR_INFORMATION_TO_SSIGNATURES_SET_FILE_AND_OBJECT_THE_IS_INFORMATION_THE_MENVIRONMENT_FOR_SUPPLY_OF_DEVEL_QALSO_CORRECTION_IN_CONTEXT_RICH_AND_IS_D_EPROVIDED_TO_PADVENT_ITS_TESTABLE_THEM_BANDWIDTH_MO_VAND_CONSOR_DATA_COMM_OAND_TO_AS_AND_S = "_serie:yan.simulation_such_back.each-man _with:vcomputing-the-of.building_key_maintains_advanced-the- _stakehol:nof.four-information.to ssignatures_set_file.:_and_object-the_is-information-the menvironment.for-supply-of.devel qalso.correction_in.context-rich_and.is_d eprovided_to_:padvent.its-testable-them.bandwidth_mo vand-consor _data.comm:oand-to.as_and-s"
    V_G20_SOFTWARE_SP_NO_COMPUTING_CASKING_FOR_IMPL_UAREA_FAN_ARE_TEST_FRAMEWORKS_TECHNICAL_WIREL_YC_VBUILDING_THE_TO_CONTEXT_R = "v:g20-software_sp _no-computing_:casking.for.impl uarea:fan.are _test-frameworks.technical_wirel yc:vbuilding_the.to.context-r"
    YC_VBUILDING_THE_TO_CONTEXT_R_ACARE_FILE_SECURITY_FILE_AREA_SOF_AS_AND_THE_INDUSTRY_SOFTWARE_AND_THE_NETWORKS_COMPETENCE_EWITH_TE_JTO_NEUTRAL_TEC_CONTAINING_USED_VISIBLY_TEST_CONSORTIUMS_THIS_SECURITY_PROF_DBASIS_AND_CONTAINS_THAT_AND_2000_PARADIGM_REVOLUTION_DES_XTHE_PERVASIVE_AUTOM_AMONG_WHICH_TO_OF_TE_AMBIGUITIES_DHELPING_HAVE_AND_VOCABU_SERIE_YAN_SIMULATION_SUCH_BACK_EACH_MAN = "yc:vbuilding_the.to.context-r acare-file.security.file_ area sof.as_and-the_industry.software.and_the_networks.competence ewith.te:jto-neutral.tec _containing_used-visibly_test.consortiums_this-security.prof dbasis_and_contains_that_and_2000.paradigm.revolution.des xthe_pervasive_autom:_among.which.to-of_te _ambiguities.:dhelping.have.and-vocabu _serie:yan.simulation_such_back.each-man"


@dataclass
class TypeAllThemSemanticsAndToolReferenceAndTheIncludeImprove:
    """
    :ivar value:
    """
    class Meta:
        name = "_all-them-semantics.and_tool-reference.and.the_include-improve"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeAndAddressingPartnershipsAAndDataTool:
    """
    :ivar value:
    """
    class Meta:
        name = "_and-addressing_partnerships.a_and_data_tool"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeContainingUsedVisiblyTestConsortiumsThisSecurityProf:
    """
    :ivar value:
    """
    class Meta:
        name = "_containing_used-visibly_test.consortiums_this-security.prof"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeHamperedOnHasBackMeasureAndBrowsersInvestigatio:
    """
    :ivar value:
    """
    class Meta:
        name = "_hampered_on_has-back_measure_and_browsers-investigatio"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeOfMustInLiesTheRequestingStructureSyst:
    """
    :ivar value:
    """
    class Meta:
        name = "_of_must_in.lies.the.requesting-structure-syst"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeSpecificationCalledCorrectio:
    """
    :ivar value:
    """
    class Meta:
        name = "_specification_called.correctio"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeTestFrameworksTechnicalWirel:
    """
    :ivar value:
    """
    class Meta:
        name = "_test-frameworks.technical_wirel"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class AcareFileSecurityFile:
    """
    :ivar value:
    """
    class Meta:
        name = "acare-file.security.file_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Area:
    """
    :ivar value:
    """
    class Meta:
        name = "area"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DbasisAndContainsThatAnd2000ParadigmRevolutionDes:
    """
    :ivar value:
    """
    class Meta:
        name = "dbasis_and_contains_that_and_2000.paradigm.revolution.des"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IisDesktopInformationIn:
    """
    :ivar value:
    """
    class Meta:
        name = "iis_desktop_information_in"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class KsupplyOfferSUsingYea:
    """
    :ivar value:
    """
    class Meta:
        name = "ksupply-offer.s-using.yea"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MenvironmentForSupplyOfDevel:
    """
    :ivar value:
    """
    class Meta:
        name = "menvironment.for-supply-of.devel"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class QalsoCorrectionInContextRichAndIsD:
    """
    :ivar value:
    """
    class Meta:
        name = "qalso.correction_in.context-rich_and.is_d"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SofAsAndTheIndustrySoftwareAndTheNetworksCompetence:
    """
    :ivar value:
    """
    class Meta:
        name = "sof.as_and-the_industry.software.and_the_networks.competence"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class VandConsor:
    """
    :ivar value:
    """
    class Meta:
        name = "vand-consor"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XcompetenceBusinessAndIsDyn:
    """
    :ivar value:
    """
    class Meta:
        name = "xcompetence.business_and.is_dyn"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvListQnameEnumeration4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-4-NS"

    value: Optional[NistschemaSvIvListQnameEnumeration4Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
