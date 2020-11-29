from tests.utils import assert_bindings


def test_introspection_introspect_test_set_introspection_1(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="common/introspection.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_nist2004_01_14_2(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="nistMeta/NISTXMLSchemaDatatypes.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_suntest_3(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/suntest.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_agroup_def_4(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AGroupDef.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_attr_decl_5(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AttrDecl.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_attr_use_6(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AttrUse.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ctype_7(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/CType.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_elem_decl_8(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/ElemDecl.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_id_constr_defs_9(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/IdConstrDefs.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_mgroup_10(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/MGroup.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_mgroup_def_11(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/MGroupDef.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_notation_12(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Notation.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_stype_13(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/SType.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_schema_14(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Schema.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_wildcard_15(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Wildcard.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_additional2006_07_15_16(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Additional_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_annotations2006_07_15_17(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Annotations_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_attribute_group2006_07_15_18(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/AttributeGroup_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_attribute2006_07_15_19(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Attribute_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_complex_type2006_07_15_20(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/ComplexType_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_data_types2006_07_15_21(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/DataTypes_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_element2006_07_15_22(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Element_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_errata102006_07_15_23(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Errata10_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_group2006_07_15_24(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Group_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_identity_constraint2006_07_15_25(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/IdentityConstraint_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_model_groups2006_07_15_26(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/ModelGroups_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_notations2006_07_15_27(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Notations_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_particles2006_07_15_28(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Particles_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_regex2006_07_15_29(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Regex_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_schema2006_07_15_30(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Schema_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_simple_type2006_07_15_31(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/SimpleType_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_ms_wildcards2006_07_15_32(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Wildcards_w3c.xml",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_boeing_xsdtest_cases_33(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="boeingMeta/BoeingXSDTestSet.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_all_34(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/All.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_assert_35(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Assert.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_complex_36(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Complex.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_cta_37(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/CTA.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_id_38(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Id.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_open_39(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Open.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_override_40(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Override.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_simple_41(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Simple.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_subsgroup_42(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Subsgroup.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_target_ns_43(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/TargetNS.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_vc_44(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/VC.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_wild_45(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Wild.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_xml_versions_46(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/XmlVersions.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_zone_47(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Zone.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_zone_48(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="oracleMeta/Zone.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_substitution_groups_49(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="wgMeta/substitution-groups.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_all_group_50(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/allGroup.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_any_attribute_51(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/anyAttribute.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_assert_52(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/assert.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_assertion_53(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/assertion.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_conditional_inclusion_54(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/conditionalInclusion.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_constraints_on_attribute_55(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/constraintsOnAttribute.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_cyclic_dependencies_redefine_include_import_override_56(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/cyclicRedefineIncludeImportOverride.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_date_57(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/date.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_date_time_stamp_58(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/dateTimeStamp.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_day_time_duration_59(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/dayTimeDuration.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_default_attributes_apply_60(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/defaultAttributesApply.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_default_fixed_61(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/defaultFixed.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_double_62(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/double.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_edcwildcard_63(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/edcWildcard.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_explicit_timezone_64(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/explicitTimezone.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_float_65(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/float.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_g_year_month_66(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gYearMonth.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_g_year_67(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gYear.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_g_month_day_68(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gMonthDay.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_g_day_69(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gDay.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_g_month_70(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gMonth.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_id_idref_71(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/idIDREF.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_identity_constraint_72(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/identityConstraint.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_list_73(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/list.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_popen_content_74(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/openContent.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_regular_expression_75(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/regularExpression.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_restriction_of_complex_types_76(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/restrictionOfComplexTypes.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_rf_white_space_77(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/rf_whiteSpace.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_substitution_group_78(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/substitutionGroup.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_target_ns_79(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/targetNamespace.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_time_80(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/time.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_type_alternative_tests_81(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/typeAlternatives.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_cta_82(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/typeAlternativesMixed.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_union_83(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/union.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_units_length_84(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/unitsLength.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_unsigned_integers_85(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/unsignedInteger.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_vc_86(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/vc.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_wildcard_87(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/wildcard.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_xml11_support_88(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xml11Support.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_xpath_default_nson_key_key_ref_unique_89(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xpathDefaultNSonKeyKeyRefUnique.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_xsimport_reference_90(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xsImportReference.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


def test_introspection_introspect_test_set_year_month_duration_91(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/yearMonthDuration.testSet",
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )
