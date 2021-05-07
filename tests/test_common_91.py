from tests.utils import assert_bindings


def test_introspection_introspect_test_set_introspection_1(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="common/introspection.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_nist2004_01_14_2(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="nistMeta/NISTXMLSchemaDatatypes.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_suntest_3(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/suntest.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_agroup_def_4(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AGroupDef.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_attr_decl_5(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AttrDecl.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_attr_use_6(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/AttrUse.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ctype_7(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/CType.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_elem_decl_8(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/ElemDecl.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_id_constr_defs_9(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/IdConstrDefs.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_mgroup_10(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/MGroup.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_mgroup_def_11(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/MGroupDef.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_notation_12(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Notation.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_stype_13(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/SType.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_schema_14(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Schema.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_wildcard_15(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="sunMeta/Wildcard.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_additional2006_07_15_16(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Additional_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_annotations2006_07_15_17(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Annotations_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_attribute_group2006_07_15_18(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/AttributeGroup_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_attribute2006_07_15_19(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Attribute_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_complex_type2006_07_15_20(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/ComplexType_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_data_types2006_07_15_21(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/DataTypes_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_element2006_07_15_22(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Element_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_errata102006_07_15_23(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Errata10_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_group2006_07_15_24(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Group_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_identity_constraint2006_07_15_25(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/IdentityConstraint_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_model_groups2006_07_15_26(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/ModelGroups_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_notations2006_07_15_27(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Notations_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_particles2006_07_15_28(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Particles_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_regex2006_07_15_29(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Regex_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_schema2006_07_15_30(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Schema_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_simple_type2006_07_15_31(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/SimpleType_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_ms_wildcards2006_07_15_32(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="msMeta/Wildcards_w3c.xml",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_boeing_xsdtest_cases_33(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="boeingMeta/BoeingXSDTestSet.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_all_34(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/All.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_assert_35(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Assert.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_complex_36(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Complex.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_cta_37(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/CTA.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_id_38(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Id.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_open_39(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Open.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_override_40(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Override.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_simple_41(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Simple.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_subsgroup_42(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Subsgroup.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_target_ns_43(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/TargetNS.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_vc_44(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/VC.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_wild_45(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Wild.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_xml_versions_46(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/XmlVersions.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_zone_47(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="saxonMeta/Zone.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_zone_48(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="oracleMeta/Zone.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_substitution_groups_49(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="wgMeta/substitution-groups.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_all_group_50(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/allGroup.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_any_attribute_51(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/anyAttribute.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_assert_52(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/assert.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_assertion_53(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/assertion.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_conditional_inclusion_54(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/conditionalInclusion.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_constraints_on_attribute_55(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/constraintsOnAttribute.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_cyclic_dependencies_redefine_include_import_override_56(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/cyclicRedefineIncludeImportOverride.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_date_57(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/date.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_date_time_stamp_58(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/dateTimeStamp.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_day_time_duration_59(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/dayTimeDuration.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_default_attributes_apply_60(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/defaultAttributesApply.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_default_fixed_61(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/defaultFixed.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_double_62(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/double.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_edcwildcard_63(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/edcWildcard.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_explicit_timezone_64(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/explicitTimezone.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_float_65(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/float.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_g_year_month_66(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gYearMonth.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_g_year_67(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gYear.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_g_month_day_68(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gMonthDay.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_g_day_69(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gDay.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_g_month_70(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/gMonth.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_id_idref_71(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/idIDREF.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_identity_constraint_72(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/identityConstraint.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_list_73(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/list.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_popen_content_74(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/openContent.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_regular_expression_75(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/regularExpression.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_restriction_of_complex_types_76(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/restrictionOfComplexTypes.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_rf_white_space_77(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/rf_whiteSpace.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_substitution_group_78(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/substitutionGroup.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_target_ns_79(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/targetNamespace.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_time_80(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/time.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_type_alternative_tests_81(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/typeAlternatives.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_cta_82(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/typeAlternativesMixed.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_union_83(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/union.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_units_length_84(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/unitsLength.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_unsigned_integers_85(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/unsignedInteger.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_vc_86(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/vc.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_wildcard_87(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/wildcard.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_xml11_support_88(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xml11Support.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_xpath_default_nson_key_key_ref_unique_89(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xpathDefaultNSonKeyKeyRefUnique.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_xsimport_reference_90(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/xsImportReference.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_introspection_introspect_test_set_year_month_duration_91(mode, save_output):

    assert_bindings(
        schema="common/xsts.xsd",
        instance="ibmMeta/yearMonthDuration.testSet",
        class_name="TestSet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )
