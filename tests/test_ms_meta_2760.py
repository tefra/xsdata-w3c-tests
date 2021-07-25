import pytest

from tests.utils import assert_bindings


def test_particles_b014_particles_b014_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB014.xsd",
        instance="msData/particles/particlesB014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b013_particles_b013_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB013.xsd",
        instance="msData/particles/particlesB013.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b010_particles_b010_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB010.xsd",
        instance="msData/particles/particlesB010.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b009_particles_b009_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB009.xsd",
        instance="msData/particles/particlesB009.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b006_particles_b006_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB006.xsd",
        instance="msData/particles/particlesB006.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b005_particles_b005_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB005.xsd",
        instance="msData/particles/particlesB005.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_b002_particles_b002_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), maxOccurs=1, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB002.xsd",
        instance="msData/particles/particlesB002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a015_particles_a015_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA015.xsd",
        instance="msData/particles/particlesA015.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a014_particles_a014_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA014.xsd",
        instance="msData/particles/particlesA014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a011_particles_a011_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA011.xsd",
        instance="msData/particles/particlesA011.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a010_particles_a010_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA010.xsd",
        instance="msData/particles/particlesA010.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a007_particles_a007_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA007.xsd",
        instance="msData/particles/particlesA007.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a006_particles_a006_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA006.xsd",
        instance="msData/particles/particlesA006.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_particles_a002_particles_a002_v(mode, save_output, output_format):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), minOccurs=1, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesA002.xsd",
        instance="msData/particles/particlesA002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_z006i_re_z006i_i(mode, save_output, output_format):
    r"""
    TEST :branch : Invalid characeter mappings from character sequence \c
    """
    assert_bindings(
        schema="msData/regex/schema_c.xsd",
        instance="msData/regex/invalid.c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_z006v_re_z006v_v(mode, save_output, output_format):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \c
    """
    assert_bindings(
        schema="msData/regex/schema_c.xsd",
        instance="msData/regex/valid.c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_z005v_re_z005v_v(mode, save_output, output_format):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \i
    """
    assert_bindings(
        schema="msData/regex/schema_i.xsd",
        instance="msData/regex/valid.i.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_z004v_re_z004v_v(mode, save_output, output_format):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \d
    """
    assert_bindings(
        schema="msData/regex/schema_d.xsd",
        instance="msData/regex/valid.d.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_z003v_re_z003v_v(mode, save_output, output_format):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \w
    """
    assert_bindings(
        schema="msData/regex/reZ003.xsd",
        instance="msData/regex/reZ003v.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_specials_specials_v(mode, save_output, output_format):
    """
    TEST :branch : Specials
    """
    assert_bindings(
        schema="msData/regex/Specials.xsd",
        instance="msData/regex/Specials.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_halfwidthand_fullwidth_forms_halfwidthand_fullwidth_forms_v(mode, save_output, output_format):
    """
    TEST :branch : HalfwidthandFullwidthForms
    """
    assert_bindings(
        schema="msData/regex/HalfwidthandFullwidthForms.xsd",
        instance="msData/regex/HalfwidthandFullwidthForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_small_form_variants_small_form_variants_v(mode, save_output, output_format):
    """
    TEST :branch : SmallFormVariants
    """
    assert_bindings(
        schema="msData/regex/SmallFormVariants.xsd",
        instance="msData/regex/SmallFormVariants.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjkcompatibility_forms_cjkcompatibility_forms_v(mode, save_output, output_format):
    """
    TEST :branch : CJKCompatibilityForms
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibilityForms.xsd",
        instance="msData/regex/CJKCompatibilityForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_combining_half_marks_combining_half_marks_v(mode, save_output, output_format):
    """
    TEST :branch : CombiningHalfMarks
    """
    assert_bindings(
        schema="msData/regex/CombiningHalfMarks.xsd",
        instance="msData/regex/CombiningHalfMarks.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_arabic_presentation_forms_a_arabic_presentation_forms_a_v(mode, save_output, output_format):
    """
    TEST :branch : ArabicPresentationForms-A
    """
    assert_bindings(
        schema="msData/regex/ArabicPresentationForms-A.xsd",
        instance="msData/regex/ArabicPresentationForms-A.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_alphabetic_presentation_forms_alphabetic_presentation_forms_v(mode, save_output, output_format):
    """
    TEST :branch : AlphabeticPresentationForms
    """
    assert_bindings(
        schema="msData/regex/AlphabeticPresentationForms.xsd",
        instance="msData/regex/AlphabeticPresentationForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjkcompatibility_ideographs_cjkcompatibility_ideographs_v(mode, save_output, output_format):
    """
    TEST :branch : CJKCompatibilityIdeographs
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibilityIdeographs.xsd",
        instance="msData/regex/CJKCompatibilityIdeographs.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_yi_radicals_yi_radicals_v(mode, save_output, output_format):
    """
    TEST :branch : YiRadicals
    """
    assert_bindings(
        schema="msData/regex/YiRadicals.xsd",
        instance="msData/regex/YiRadicals.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_yi_syllables_yi_syllables_v(mode, save_output, output_format):
    """
    TEST :branch : YiSyllables
    """
    assert_bindings(
        schema="msData/regex/YiSyllables.xsd",
        instance="msData/regex/YiSyllables.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjkunified_ideographs_cjkunified_ideographs_v(mode, save_output, output_format):
    """
    TEST :branch : CJKUnifiedIdeographs
    """
    assert_bindings(
        schema="msData/regex/CJKUnifiedIdeographs.xsd",
        instance="msData/regex/CJKUnifiedIdeographs.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjkcompatibility_cjkcompatibility_v(mode, save_output, output_format):
    """
    TEST :branch : CJKCompatibility
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibility.xsd",
        instance="msData/regex/CJKCompatibility.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_enclosed_cjklettersand_months_enclosed_cjklettersand_months_v(mode, save_output, output_format):
    """
    TEST :branch : EnclosedCJKLettersandMonths
    """
    assert_bindings(
        schema="msData/regex/EnclosedCJKLettersandMonths.xsd",
        instance="msData/regex/EnclosedCJKLettersandMonths.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_bopomofo_extended_bopomofo_extended_v(mode, save_output, output_format):
    """
    TEST :branch : BopomofoExtended
    """
    assert_bindings(
        schema="msData/regex/BopomofoExtended.xsd",
        instance="msData/regex/BopomofoExtended.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_kanbun_kanbun_v(mode, save_output, output_format):
    """
    TEST :branch : Kanbun
    """
    assert_bindings(
        schema="msData/regex/Kanbun.xsd",
        instance="msData/regex/Kanbun.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_hangul_compatibility_jamo_hangul_compatibility_jamo_v(mode, save_output, output_format):
    """
    TEST :branch : HangulCompatibilityJamo
    """
    assert_bindings(
        schema="msData/regex/HangulCompatibilityJamo.xsd",
        instance="msData/regex/HangulCompatibilityJamo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_bopomofo_bopomofo_v(mode, save_output, output_format):
    """
    TEST :branch : Bopomofo
    """
    assert_bindings(
        schema="msData/regex/Bopomofo.xsd",
        instance="msData/regex/Bopomofo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_katakana_katakana_v(mode, save_output, output_format):
    """
    TEST :branch : Katakana
    """
    assert_bindings(
        schema="msData/regex/Katakana.xsd",
        instance="msData/regex/Katakana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_hiragana_hiragana_v(mode, save_output, output_format):
    """
    TEST :branch : Hiragana
    """
    assert_bindings(
        schema="msData/regex/Hiragana.xsd",
        instance="msData/regex/Hiragana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjksymbolsand_punctuation_cjksymbolsand_punctuation_v(mode, save_output, output_format):
    """
    TEST :branch : CJKSymbolsandPunctuation
    """
    assert_bindings(
        schema="msData/regex/CJKSymbolsandPunctuation.xsd",
        instance="msData/regex/CJKSymbolsandPunctuation.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ideographic_description_characters_ideographic_description_characters_v(mode, save_output, output_format):
    """
    TEST :branch : IdeographicDescriptionCharacters
    """
    assert_bindings(
        schema="msData/regex/IdeographicDescriptionCharacters.xsd",
        instance="msData/regex/IdeographicDescriptionCharacters.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_kangxi_radicals_kangxi_radicals_v(mode, save_output, output_format):
    """
    TEST :branch : KangxiRadicals
    """
    assert_bindings(
        schema="msData/regex/KangxiRadicals.xsd",
        instance="msData/regex/KangxiRadicals.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cjkradicals_supplement_cjkradicals_supplement_v(mode, save_output, output_format):
    """
    TEST :branch : CJKRadicalsSupplement
    """
    assert_bindings(
        schema="msData/regex/CJKRadicalsSupplement.xsd",
        instance="msData/regex/CJKRadicalsSupplement.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_braille_patterns_braille_patterns_v(mode, save_output, output_format):
    """
    TEST :branch : BraillePatterns
    """
    assert_bindings(
        schema="msData/regex/BraillePatterns.xsd",
        instance="msData/regex/BraillePatterns.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_dingbats_dingbats_v(mode, save_output, output_format):
    """
    TEST :branch : Dingbats
    """
    assert_bindings(
        schema="msData/regex/Dingbats.xsd",
        instance="msData/regex/Dingbats.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_miscellaneous_symbols_miscellaneous_symbols_v(mode, save_output, output_format):
    """
    TEST :branch : MiscellaneousSymbols
    """
    assert_bindings(
        schema="msData/regex/MiscellaneousSymbols.xsd",
        instance="msData/regex/MiscellaneousSymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_geometric_shapes_geometric_shapes_v(mode, save_output, output_format):
    """
    TEST :branch : GeometricShapes
    """
    assert_bindings(
        schema="msData/regex/GeometricShapes.xsd",
        instance="msData/regex/GeometricShapes.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_block_elements_block_elements_v(mode, save_output, output_format):
    """
    TEST :branch : BlockElements
    """
    assert_bindings(
        schema="msData/regex/BlockElements.xsd",
        instance="msData/regex/BlockElements.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_box_drawing_box_drawing_v(mode, save_output, output_format):
    """
    TEST :branch : BoxDrawing
    """
    assert_bindings(
        schema="msData/regex/BoxDrawing.xsd",
        instance="msData/regex/BoxDrawing.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_enclosed_alphanumerics_enclosed_alphanumerics_v(mode, save_output, output_format):
    """
    TEST :branch : EnclosedAlphanumerics
    """
    assert_bindings(
        schema="msData/regex/EnclosedAlphanumerics.xsd",
        instance="msData/regex/EnclosedAlphanumerics.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_optical_character_recognition_optical_character_recognition_v(mode, save_output, output_format):
    """
    TEST :branch : OpticalCharacterRecognition
    """
    assert_bindings(
        schema="msData/regex/OpticalCharacterRecognition.xsd",
        instance="msData/regex/OpticalCharacterRecognition.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_control_pictures_control_pictures_v(mode, save_output, output_format):
    """
    TEST :branch : ControlPictures
    """
    assert_bindings(
        schema="msData/regex/ControlPictures.xsd",
        instance="msData/regex/ControlPictures.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_miscellaneous_technical_miscellaneous_technical_v(mode, save_output, output_format):
    """
    TEST :branch : MiscellaneousTechnical
    """
    assert_bindings(
        schema="msData/regex/MiscellaneousTechnical.xsd",
        instance="msData/regex/MiscellaneousTechnical.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_mathematical_operators_mathematical_operators_v(mode, save_output, output_format):
    """
    TEST :branch : MathematicalOperators
    """
    assert_bindings(
        schema="msData/regex/MathematicalOperators.xsd",
        instance="msData/regex/MathematicalOperators.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_arrows_arrows_v(mode, save_output, output_format):
    """
    TEST :branch : Arrows
    """
    assert_bindings(
        schema="msData/regex/Arrows.xsd",
        instance="msData/regex/Arrows.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_number_forms_number_forms_v(mode, save_output, output_format):
    """
    TEST :branch : NumberForms
    """
    assert_bindings(
        schema="msData/regex/NumberForms.xsd",
        instance="msData/regex/NumberForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_letterlike_symbols_letterlike_symbols_v(mode, save_output, output_format):
    """
    TEST :branch : LetterlikeSymbols
    """
    assert_bindings(
        schema="msData/regex/LetterlikeSymbols.xsd",
        instance="msData/regex/LetterlikeSymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_currency_symbols_currency_symbols_v(mode, save_output, output_format):
    """
    TEST :branch : CurrencySymbols
    """
    assert_bindings(
        schema="msData/regex/CurrencySymbols.xsd",
        instance="msData/regex/CurrencySymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_superscriptsand_subscripts_superscriptsand_subscripts_v(mode, save_output, output_format):
    """
    TEST :branch : SuperscriptsandSubscripts
    """
    assert_bindings(
        schema="msData/regex/SuperscriptsandSubscripts.xsd",
        instance="msData/regex/SuperscriptsandSubscripts.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_general_punctuation_general_punctuation_v(mode, save_output, output_format):
    """
    TEST :branch : GeneralPunctuation
    """
    assert_bindings(
        schema="msData/regex/GeneralPunctuation.xsd",
        instance="msData/regex/GeneralPunctuation.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_greek_extended_greek_extended_v(mode, save_output, output_format):
    """
    TEST :branch : GreekExtended
    """
    assert_bindings(
        schema="msData/regex/GreekExtended.xsd",
        instance="msData/regex/GreekExtended.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_latin_extended_additional_latin_extended_additional_v(mode, save_output, output_format):
    """
    TEST :branch : LatinExtendedAdditional
    """
    assert_bindings(
        schema="msData/regex/LatinExtendedAdditional.xsd",
        instance="msData/regex/LatinExtendedAdditional.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_mongolian_mongolian_v(mode, save_output, output_format):
    """
    TEST :branch : Mongolian
    """
    assert_bindings(
        schema="msData/regex/Mongolian.xsd",
        instance="msData/regex/Mongolian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_khmer_khmer_v(mode, save_output, output_format):
    """
    TEST :branch : Khmer
    """
    assert_bindings(
        schema="msData/regex/Khmer.xsd",
        instance="msData/regex/Khmer.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_runic_runic_v(mode, save_output, output_format):
    """
    TEST :branch : Runic
    """
    assert_bindings(
        schema="msData/regex/Runic.xsd",
        instance="msData/regex/Runic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ogham_ogham_v(mode, save_output, output_format):
    """
    TEST :branch : Ogham
    """
    assert_bindings(
        schema="msData/regex/Ogham.xsd",
        instance="msData/regex/Ogham.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_unified_canadian_aboriginal_syllabics_unified_canadian_aboriginal_syllabics_v(mode, save_output, output_format):
    """
    TEST :branch : UnifiedCanadianAboriginalSyllabics
    """
    assert_bindings(
        schema="msData/regex/UnifiedCanadianAboriginalSyllabics.xsd",
        instance="msData/regex/UnifiedCanadianAboriginalSyllabics.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cherokee_cherokee_v(mode, save_output, output_format):
    """
    TEST :branch : Cherokee
    """
    assert_bindings(
        schema="msData/regex/Cherokee.xsd",
        instance="msData/regex/Cherokee.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ethiopic_ethiopic_v(mode, save_output, output_format):
    """
    TEST :branch : Ethiopic
    """
    assert_bindings(
        schema="msData/regex/Ethiopic.xsd",
        instance="msData/regex/Ethiopic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_hangul_jamo_hangul_jamo_v(mode, save_output, output_format):
    """
    TEST :branch : HangulJamo
    """
    assert_bindings(
        schema="msData/regex/HangulJamo.xsd",
        instance="msData/regex/HangulJamo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_georgian_georgian_v(mode, save_output, output_format):
    """
    TEST :branch : Georgian
    """
    assert_bindings(
        schema="msData/regex/Georgian.xsd",
        instance="msData/regex/Georgian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_myanmar_myanmar_v(mode, save_output, output_format):
    """
    TEST :branch : Myanmar
    """
    assert_bindings(
        schema="msData/regex/Myanmar.xsd",
        instance="msData/regex/Myanmar.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_tibetan_tibetan_v(mode, save_output, output_format):
    """
    TEST :branch : Tibetan
    """
    assert_bindings(
        schema="msData/regex/Tibetan.xsd",
        instance="msData/regex/Tibetan.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_lao_lao_v(mode, save_output, output_format):
    """
    TEST :branch : Lao
    """
    assert_bindings(
        schema="msData/regex/Lao.xsd",
        instance="msData/regex/Lao.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_thai_thai_v(mode, save_output, output_format):
    """
    TEST :branch : Thai
    """
    assert_bindings(
        schema="msData/regex/Thai.xsd",
        instance="msData/regex/Thai.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sinhala_sinhala_v(mode, save_output, output_format):
    """
    TEST :branch : Sinhala
    """
    assert_bindings(
        schema="msData/regex/Sinhala.xsd",
        instance="msData/regex/Sinhala.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_malayalam_malayalam_v(mode, save_output, output_format):
    """
    TEST :branch : Malayalam
    """
    assert_bindings(
        schema="msData/regex/Malayalam.xsd",
        instance="msData/regex/Malayalam.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_kannada_kannada_v(mode, save_output, output_format):
    """
    TEST :branch : Kannada
    """
    assert_bindings(
        schema="msData/regex/Kannada.xsd",
        instance="msData/regex/Kannada.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_telugu_telugu_v(mode, save_output, output_format):
    """
    TEST :branch : Telugu
    """
    assert_bindings(
        schema="msData/regex/Telugu.xsd",
        instance="msData/regex/Telugu.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_tamil_tamil_v(mode, save_output, output_format):
    """
    TEST :branch : Tamil
    """
    assert_bindings(
        schema="msData/regex/Tamil.xsd",
        instance="msData/regex/Tamil.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_oriya_oriya_v(mode, save_output, output_format):
    """
    TEST :branch : Oriya
    """
    assert_bindings(
        schema="msData/regex/Oriya.xsd",
        instance="msData/regex/Oriya.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_gujarati_gujarati_v(mode, save_output, output_format):
    """
    TEST :branch : Gujarati
    """
    assert_bindings(
        schema="msData/regex/Gujarati.xsd",
        instance="msData/regex/Gujarati.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_gurmukhi_gurmukhi_v(mode, save_output, output_format):
    """
    TEST :branch : Gurmukhi
    """
    assert_bindings(
        schema="msData/regex/Gurmukhi.xsd",
        instance="msData/regex/Gurmukhi.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_bengali_bengali_v(mode, save_output, output_format):
    """
    TEST :branch : Bengali
    """
    assert_bindings(
        schema="msData/regex/Bengali.xsd",
        instance="msData/regex/Bengali.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_devanagari_devanagari_v(mode, save_output, output_format):
    """
    TEST :branch : Devanagari
    """
    assert_bindings(
        schema="msData/regex/Devanagari.xsd",
        instance="msData/regex/Devanagari.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_thaana_thaana_v(mode, save_output, output_format):
    """
    TEST :branch : Thaana
    """
    assert_bindings(
        schema="msData/regex/Thaana.xsd",
        instance="msData/regex/Thaana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_syriac_syriac_v(mode, save_output, output_format):
    """
    TEST :branch : Syriac
    """
    assert_bindings(
        schema="msData/regex/Syriac.xsd",
        instance="msData/regex/Syriac.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_arabic_arabic_v(mode, save_output, output_format):
    """
    TEST :branch : Arabic
    """
    assert_bindings(
        schema="msData/regex/Arabic.xsd",
        instance="msData/regex/Arabic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_hebrew_hebrew_v(mode, save_output, output_format):
    """
    TEST :branch : Hebrew
    """
    assert_bindings(
        schema="msData/regex/Hebrew.xsd",
        instance="msData/regex/Hebrew.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_armenian_armenian_v(mode, save_output, output_format):
    """
    TEST :branch : Armenian
    """
    assert_bindings(
        schema="msData/regex/Armenian.xsd",
        instance="msData/regex/Armenian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cyrillic_cyrillic_v(mode, save_output, output_format):
    """
    TEST :branch : Cyrillic
    """
    assert_bindings(
        schema="msData/regex/Cyrillic.xsd",
        instance="msData/regex/Cyrillic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_combining_diacritical_marks_combining_diacritical_marks_v(mode, save_output, output_format):
    """
    TEST :branch : CombiningDiacriticalMarks
    """
    assert_bindings(
        schema="msData/regex/CombiningDiacriticalMarks.xsd",
        instance="msData/regex/CombiningDiacriticalMarks.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_spacing_modifier_letters_spacing_modifier_letters_v(mode, save_output, output_format):
    """
    TEST :branch : SpacingModifierLetters
    """
    assert_bindings(
        schema="msData/regex/SpacingModifierLetters.xsd",
        instance="msData/regex/SpacingModifierLetters.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ipaextensions_ipaextensions_v(mode, save_output, output_format):
    """
    TEST :branch : IPAExtensions
    """
    assert_bindings(
        schema="msData/regex/IPAExtensions.xsd",
        instance="msData/regex/IPAExtensions.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_latin_extended_b_latin_extended_b_v(mode, save_output, output_format):
    """
    TEST :branch : LatinExtended-B
    """
    assert_bindings(
        schema="msData/regex/LatinExtended-B.xsd",
        instance="msData/regex/LatinExtended-B.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_latin_extended_a_latin_extended_a_v(mode, save_output, output_format):
    """
    TEST :branch : LatinExtended-A
    """
    assert_bindings(
        schema="msData/regex/LatinExtended-A.xsd",
        instance="msData/regex/LatinExtended-A.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_latin_1_supplement_latin_1_supplement_v(mode, save_output, output_format):
    """
    TEST :branch : Latin-1Supplement
    """
    assert_bindings(
        schema="msData/regex/Latin-1Supplement.xsd",
        instance="msData/regex/Latin-1Supplement.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_basic_latin_basic_latin_v(mode, save_output, output_format):
    """
    TEST :branch : BasicLatin
    """
    assert_bindings(
        schema="msData/regex/BasicLatin.xsd",
        instance="msData/regex/BasicLatin.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_535_regex_test_535_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_535
    """
    assert_bindings(
        schema="msData/regex/RegexTest_535.xsd",
        instance="msData/regex/RegexTest_535.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_530_regex_test_530_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_530
    """
    assert_bindings(
        schema="msData/regex/RegexTest_530.xsd",
        instance="msData/regex/RegexTest_530.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_525_regex_test_525_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_525
    """
    assert_bindings(
        schema="msData/regex/RegexTest_525.xsd",
        instance="msData/regex/RegexTest_525.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_522_regex_test_522_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_522
    """
    assert_bindings(
        schema="msData/regex/RegexTest_522.xsd",
        instance="msData/regex/RegexTest_522.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_515_regex_test_515_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_515
    """
    assert_bindings(
        schema="msData/regex/RegexTest_515.xsd",
        instance="msData/regex/RegexTest_515.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_513_regex_test_513_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_513
    """
    assert_bindings(
        schema="msData/regex/RegexTest_513.xsd",
        instance="msData/regex/RegexTest_513.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_495_regex_test_495_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_495
    """
    assert_bindings(
        schema="msData/regex/RegexTest_495.xsd",
        instance="msData/regex/RegexTest_495.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_319_regex_test_319_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_319
    """
    assert_bindings(
        schema="msData/regex/RegexTest_319.xsd",
        instance="msData/regex/RegexTest_319.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_264_regex_test_264_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_264
    """
    assert_bindings(
        schema="msData/regex/RegexTest_264.xsd",
        instance="msData/regex/RegexTest_264.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_263_regex_test_263_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_263
    """
    assert_bindings(
        schema="msData/regex/RegexTest_263.xsd",
        instance="msData/regex/RegexTest_263.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_262_regex_test_262_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_262
    """
    assert_bindings(
        schema="msData/regex/RegexTest_262.xsd",
        instance="msData/regex/RegexTest_262.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_261_regex_test_261_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_261
    """
    assert_bindings(
        schema="msData/regex/RegexTest_261.xsd",
        instance="msData/regex/RegexTest_261.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_260_regex_test_260_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_260
    """
    assert_bindings(
        schema="msData/regex/RegexTest_260.xsd",
        instance="msData/regex/RegexTest_260.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_259_regex_test_259_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_259
    """
    assert_bindings(
        schema="msData/regex/RegexTest_259.xsd",
        instance="msData/regex/RegexTest_259.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_234_regex_test_234_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_234
    """
    assert_bindings(
        schema="msData/regex/RegexTest_234.xsd",
        instance="msData/regex/RegexTest_234.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_81_regex_test_81_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_81
    """
    assert_bindings(
        schema="msData/regex/RegexTest_81.xsd",
        instance="msData/regex/RegexTest_81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_80_regex_test_80_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_80
    """
    assert_bindings(
        schema="msData/regex/RegexTest_80.xsd",
        instance="msData/regex/RegexTest_80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_73_regex_test_73_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_73
    """
    assert_bindings(
        schema="msData/regex/RegexTest_73.xsd",
        instance="msData/regex/RegexTest_73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_72_regex_test_72_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_72
    """
    assert_bindings(
        schema="msData/regex/RegexTest_72.xsd",
        instance="msData/regex/RegexTest_72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_42_regex_test_42_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_42
    """
    assert_bindings(
        schema="msData/regex/RegexTest_42.xsd",
        instance="msData/regex/RegexTest_42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_41_regex_test_41_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_41
    """
    assert_bindings(
        schema="msData/regex/RegexTest_41.xsd",
        instance="msData/regex/RegexTest_41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_21_regex_test_21_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_21
    """
    assert_bindings(
        schema="msData/regex/RegexTest_21.xsd",
        instance="msData/regex/RegexTest_21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_20_regex_test_20_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_20
    """
    assert_bindings(
        schema="msData/regex/RegexTest_20.xsd",
        instance="msData/regex/RegexTest_20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_6_regex_test_6_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_6
    """
    assert_bindings(
        schema="msData/regex/RegexTest_6.xsd",
        instance="msData/regex/RegexTest_6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_5_regex_test_5_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_5
    """
    assert_bindings(
        schema="msData/regex/RegexTest_5.xsd",
        instance="msData/regex/RegexTest_5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_4_regex_test_4_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_4
    """
    assert_bindings(
        schema="msData/regex/RegexTest_4.xsd",
        instance="msData/regex/RegexTest_4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_3_regex_test_3_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_3
    """
    assert_bindings(
        schema="msData/regex/RegexTest_3.xsd",
        instance="msData/regex/RegexTest_3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_2_regex_test_2_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_2
    """
    assert_bindings(
        schema="msData/regex/RegexTest_2.xsd",
        instance="msData/regex/RegexTest_2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_regex_test_1_regex_test_1_v(mode, save_output, output_format):
    """
    TEST :branch : RegexTest_1
    """
    assert_bindings(
        schema="msData/regex/RegexTest_1.xsd",
        instance="msData/regex/RegexTest_1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p20_p20_v(mode, save_output, output_format):
    """
    TEST :branch : restriction of two patterns in a simple type (1)
    "[abc]+" (2) "[123]+", should allow only the intersection, value="a1"
    [invalid]
    """
    assert_bindings(
        schema="msData/regex/p20.xsd",
        instance="msData/regex/p20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p17_p17_v(mode, save_output, output_format):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="abcaabbccabc"
    [valid]
    """
    assert_bindings(
        schema="msData/regex/p17.xsd",
        instance="msData/regex/p17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p16_p16_v(mode, save_output, output_format):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="112233123" [valid]
    """
    assert_bindings(
        schema="msData/regex/p16.xsd",
        instance="msData/regex/p16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p13_p13_v(mode, save_output, output_format):
    r"""
    TEST :branch : regex\pattern=123]+|[abc]+, value=abcaabbccabc [valid]
    """
    assert_bindings(
        schema="msData/regex/p13.xsd",
        instance="msData/regex/p13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p12_p12_v(mode, save_output, output_format):
    """
    TEST :branch :
    """
    assert_bindings(
        schema="msData/regex/p12.xsd",
        instance="msData/regex/p12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p11_p11_v(mode, save_output, output_format):
    r"""
    TEST :branch : regex\restriction of a type that defined as emum
    {1,2,3}, pattern="[13]", XML has value=3 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p11.xsd",
        instance="msData/regex/p11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p9_p9_v(mode, save_output, output_format):
    r"""
    TEST :branch : regex\restriction of a type that defined as emum
    {1,2,3}, pattern="[13]", XML has value=1 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p9.xsd",
        instance="msData/regex/p9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p8_p8_v(mode, save_output, output_format):
    r"""
    TEST :branch : restriction of a type that defined as integer,
    minInclusive=-9, pattern="\-[0-9]*", XML has value=-9 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p8.xsd",
        instance="msData/regex/p8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p6_p6_v(mode, save_output, output_format):
    r"""
    TEST :branch : regex\restriction of a type that defined as integer,
    maxExclusive=10, pattern="\-[0-9]*", XML has value=-1 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p6.xsd",
        instance="msData/regex/p6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p5_p5_v(mode, save_output, output_format):
    """
    TEST :branch : restriction of a type that defined as integer,
    maxExclusive=10, pattern="[0-9]*", XML has value=0 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p5.xsd",
        instance="msData/regex/p5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_p3_p3_v(mode, save_output, output_format):
    """
    TEST :branch : restriction of a type that defined as integer,
    maxExclusive=10, pattern="[0-9]*", XML has value=9 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p3.xsd",
        instance="msData/regex/p3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di14_re_di14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='positiveInteger', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI14.xsd",
        instance="msData/regex/reDI14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di11_re_di11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='unsignedInt', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI11.xsd",
        instance="msData/regex/reDI11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di10_re_di10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='unsignedLong', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI10.xsd",
        instance="msData/regex/reDI10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di9_re_di9_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='nonNegativeInteger', pattern='\d+', value='1111',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI9.xsd",
        instance="msData/regex/reDI9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di8_re_di8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='byte', pattern='(\- |
    \+)?((1[0-2]?[0-7]?)|([1-9]?[0-9]?))|(\+?128)', value='128',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI8.xsd",
        instance="msData/regex/reDI8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di7_re_di7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='short', pattern='\-?[0-3]{3}', value='-300',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI7.xsd",
        instance="msData/regex/reDI7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di6_re_di6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='int', pattern='\d+', value='123', type='valid',
    RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI6.xsd",
        instance="msData/regex/reDI6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di2_re_di2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='integer', pattern='\p{Nd}+', value='10000201',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI2.xsd",
        instance="msData/regex/reDI2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_di1_re_di1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='decimal', pattern='\p{Nd}+', value='10000101',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI1.xsd",
        instance="msData/regex/reDI1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh11_re_dh11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='NMTOKEN', pattern='\c[\c\d]*', value='name1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH11.xsd",
        instance="msData/regex/reDH11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh7_re_dh7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='IDREF', pattern='\c[\c\d]*', value='ab',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH7.xsd",
        instance="msData/regex/reDH7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh6_re_dh6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='ID', pattern='\c[\c\d]*', value='a1b',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH6.xsd",
        instance="msData/regex/reDH6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh5_re_dh5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='NCName', pattern='[\i-[:]][\c-[:]]*',
    value='a:b', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH5.xsd",
        instance="msData/regex/reDH5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh4_re_dh4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='Name', pattern='\c+', value='abcdef',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH4.xsd",
        instance="msData/regex/reDH4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh3_re_dh3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='language', pattern='\c{2,4}', value='ch-a',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH3.xsd",
        instance="msData/regex/reDH3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dh2_re_dh2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='token', pattern='\c+', value='a', type='valid',
    RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH2.xsd",
        instance="msData/regex/reDH2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dg7_re_dg7_v(mode, save_output, output_format):
    """
    TEST :branch : base='gMonth', pattern='[123456789]|(10|11|12)',
    value='9', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG7.xsd",
        instance="msData/regex/reDG7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dg6_re_dg6_v(mode, save_output, output_format):
    """
    TEST :branch : base='gDay', pattern='([123]0)|([12]?[1-9])|(31)',
    value='30', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG6.xsd",
        instance="msData/regex/reDG6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dg5_re_dg5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='gMonthDay', pattern='0[123]\-(12|14)',
    value='03-14', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG5.xsd",
        instance="msData/regex/reDG5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dg3_re_dg3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='gYear', pattern='\p{Nd}{4}', value='1999',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG3.xsd",
        instance="msData/regex/reDG3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dg1_re_dg1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='date', pattern='\p{Nd}{4}-\p{Nd}{2}-\p{Nd}{2}',
    value='1999-12-12', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG1.xsd",
        instance="msData/regex/reDG1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_df2_re_df2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='time',
    pattern='\p{Nd}{2}:\d\d:\d\d(\-\d\d:\d\d)?', value='13:20:00-5:00',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF2.xsd",
        instance="msData/regex/reDF2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_df1_re_df1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='time',
    pattern='\p{Nd}{2}:\d\d:\d\d(\-\d\d:\d\d)?', value='11:00:00',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF1.xsd",
        instance="msData/regex/reDF1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_de1_re_de1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='dateTime',
    pattern='\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d',
    value='2001-06-06T12:12:00', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDE1.xsd",
        instance="msData/regex/reDE1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dd1_re_dd1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P1111Y12M', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD1.xsd",
        instance="msData/regex/reDD1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dc5_re_dc5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='Qname',
    pattern='[\i-[:]][\c-[:]]+:[\i-[:]][\c-[:]]+', value='a:b',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC5.xsd",
        instance="msData/regex/reDC5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dc4_re_dc4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='anyURI', pattern='http://\c*',
    value='http://www.foo.com', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC4.xsd",
        instance="msData/regex/reDC4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dc3_re_dc3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='double', pattern='\d*\.\d+', value='1.001',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC3.xsd",
        instance="msData/regex/reDC3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dc2_re_dc2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='float', pattern='\d*\.\d+', value='1.001',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC2.xsd",
        instance="msData/regex/reDC2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_dc1_re_dc1_v(mode, save_output, output_format):
    """
    TEST :branch : base='hexBinary', pattern='AF01D1', value='AF01D1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC1.xsd",
        instance="msData/regex/reDC1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_db2_re_db2_v(mode, save_output, output_format):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='110100111', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB2.xsd",
        instance="msData/regex/reDB2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_db1_re_db1_v(mode, save_output, output_format):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='1111', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB1.xsd",
        instance="msData/regex/reDB1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da15_re_da15_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='(1|true|false|0|0)',
    value='0', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA15.xsd",
        instance="msData/regex/reDA15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da9_re_da9_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA9.xsd",
        instance="msData/regex/reDA9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da6_re_da6_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='(true|false)', value='false',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA6.xsd",
        instance="msData/regex/reDA6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da5_re_da5_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='(true|false)', value='true',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA5.xsd",
        instance="msData/regex/reDA5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da4_re_da4_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='false', value='false',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA4.xsd",
        instance="msData/regex/reDA4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_da1_re_da1_v(mode, save_output, output_format):
    """
    TEST :branch : base='boolean', pattern='true', value='true',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA1.xsd",
        instance="msData/regex/reDA1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_u6_re_u6_i(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x023F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU6.xsd",
        instance="msData/regex/reU6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t83_re_t83_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF1A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT83.xsd",
        instance="msData/regex/reT83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t82_re_t82_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x181A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT82.xsd",
        instance="msData/regex/reT82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t81_re_t81_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17EA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT81.xsd",
        instance="msData/regex/reT81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t80_re_t80_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1372;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT80.xsd",
        instance="msData/regex/reT80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t79_re_t79_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x104A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT79.xsd",
        instance="msData/regex/reT79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t78_re_t78_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F2A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT78.xsd",
        instance="msData/regex/reT78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t77_re_t77_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0EDA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT77.xsd",
        instance="msData/regex/reT77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t76_re_t76_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E5A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT76.xsd",
        instance="msData/regex/reT76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t75_re_t75_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT75.xsd",
        instance="msData/regex/reT75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t74_re_t74_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT74.xsd",
        instance="msData/regex/reT74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t73_re_t73_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT73.xsd",
        instance="msData/regex/reT73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t72_re_t72_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT72.xsd",
        instance="msData/regex/reT72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t71_re_t71_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0B70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT71.xsd",
        instance="msData/regex/reT71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t70_re_t70_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT70.xsd",
        instance="msData/regex/reT70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t69_re_t69_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0A79;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT69.xsd",
        instance="msData/regex/reT69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t68_re_t68_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09F0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT68.xsd",
        instance="msData/regex/reT68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t67_re_t67_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0970;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT67.xsd",
        instance="msData/regex/reT67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t66_re_t66_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06FA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT66.xsd",
        instance="msData/regex/reT66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t65_re_t65_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x066A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT65.xsd",
        instance="msData/regex/reT65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t64_re_t64_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x003A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT64.xsd",
        instance="msData/regex/reT64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t62_re_t62_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF09;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT62.xsd",
        instance="msData/regex/reT62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t61_re_t61_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1809;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT61.xsd",
        instance="msData/regex/reT61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t60_re_t60_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17DF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT60.xsd",
        instance="msData/regex/reT60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t59_re_t59_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1368;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT59.xsd",
        instance="msData/regex/reT59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t58_re_t58_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1039;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT58.xsd",
        instance="msData/regex/reT58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t57_re_t57_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F19;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT57.xsd",
        instance="msData/regex/reT57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t56_re_t56_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0ECF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT56.xsd",
        instance="msData/regex/reT56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t55_re_t55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E49;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT55.xsd",
        instance="msData/regex/reT55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t54_re_t54_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT54.xsd",
        instance="msData/regex/reT54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t53_re_t53_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CE5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT53.xsd",
        instance="msData/regex/reT53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t52_re_t52_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT52.xsd",
        instance="msData/regex/reT52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t51_re_t51_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT51.xsd",
        instance="msData/regex/reT51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t50_re_t50_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0B65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT50.xsd",
        instance="msData/regex/reT50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t49_re_t49_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AE5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT49.xsd",
        instance="msData/regex/reT49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t48_re_t48_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0A65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT48.xsd",
        instance="msData/regex/reT48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t47_re_t47_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09E5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT47.xsd",
        instance="msData/regex/reT47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t46_re_t46_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0965;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT46.xsd",
        instance="msData/regex/reT46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t45_re_t45_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06EE;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT45.xsd",
        instance="msData/regex/reT45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t44_re_t44_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0659;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT44.xsd",
        instance="msData/regex/reT44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t43_re_t43_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0029;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT43.xsd",
        instance="msData/regex/reT43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t38_re_t38_i(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1371;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT38.xsd",
        instance="msData/regex/reT38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_t17_re_t17_i(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1369;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT17.xsd",
        instance="msData/regex/reT17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s51_re_s51_i(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BE6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS51.xsd",
        instance="msData/regex/reS51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s41_re_s41_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF19;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS41.xsd",
        instance="msData/regex/reS41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s40_re_s40_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1819;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS40.xsd",
        instance="msData/regex/reS40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s39_re_s39_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17E9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS39.xsd",
        instance="msData/regex/reS39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s38_re_s38_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1371;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS38.xsd",
        instance="msData/regex/reS38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s37_re_s37_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1049;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS37.xsd",
        instance="msData/regex/reS37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s36_re_s36_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F29;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS36.xsd",
        instance="msData/regex/reS36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s35_re_s35_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0ED9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS35.xsd",
        instance="msData/regex/reS35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s34_re_s34_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E59;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS34.xsd",
        instance="msData/regex/reS34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s33_re_s33_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS33.xsd",
        instance="msData/regex/reS33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s32_re_s32_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS32.xsd",
        instance="msData/regex/reS32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s31_re_s31_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS31.xsd",
        instance="msData/regex/reS31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s30_re_s30_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS30.xsd",
        instance="msData/regex/reS30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s29_re_s29_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS29.xsd",
        instance="msData/regex/reS29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s28_re_s28_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS28.xsd",
        instance="msData/regex/reS28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s27_re_s27_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS27.xsd",
        instance="msData/regex/reS27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s26_re_s26_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09EF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS26.xsd",
        instance="msData/regex/reS26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s25_re_s25_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x096F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS25.xsd",
        instance="msData/regex/reS25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s24_re_s24_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06F9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS24.xsd",
        instance="msData/regex/reS24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s23_re_s23_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0669;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS23.xsd",
        instance="msData/regex/reS23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s22_re_s22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0039;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS22.xsd",
        instance="msData/regex/reS22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s20_re_s20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF10;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS20.xsd",
        instance="msData/regex/reS20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s19_re_s19_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1810;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS19.xsd",
        instance="msData/regex/reS19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s18_re_s18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17E0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS18.xsd",
        instance="msData/regex/reS18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s17_re_s17_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1369;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS17.xsd",
        instance="msData/regex/reS17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s16_re_s16_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1040;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS16.xsd",
        instance="msData/regex/reS16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s15_re_s15_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS15.xsd",
        instance="msData/regex/reS15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s14_re_s14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0ED0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS14.xsd",
        instance="msData/regex/reS14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s13_re_s13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E50;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS13.xsd",
        instance="msData/regex/reS13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s12_re_s12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS12.xsd",
        instance="msData/regex/reS12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s11_re_s11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS11.xsd",
        instance="msData/regex/reS11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s10_re_s10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS10.xsd",
        instance="msData/regex/reS10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s9_re_s9_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BE7;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS9.xsd",
        instance="msData/regex/reS9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s8_re_s8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS8.xsd",
        instance="msData/regex/reS8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s7_re_s7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS7.xsd",
        instance="msData/regex/reS7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s6_re_s6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS6.xsd",
        instance="msData/regex/reS6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s5_re_s5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09E6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS5.xsd",
        instance="msData/regex/reS5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s3_re_s3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06F0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS3.xsd",
        instance="msData/regex/reS3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_s1_re_s1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0030;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS1.xsd",
        instance="msData/regex/reS1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r25_re_r25_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*', value='aa2a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR25.xsd",
        instance="msData/regex/reR25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r24_re_r24_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='a1a2a3', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR24.xsd",
        instance="msData/regex/reR24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r22_re_r22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\C', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR22.xsd",
        instance="msData/regex/reR22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r21_re_r21_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\C', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR21.xsd",
        instance="msData/regex/reR21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r20_re_r20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\C', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR20.xsd",
        instance="msData/regex/reR20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r19_re_r19_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\C', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR19.xsd",
        instance="msData/regex/reR19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r14_re_r14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*',
    value='aaaaaaaaaaaaaaaaaaaaaaaaaa', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR14.xsd",
        instance="msData/regex/reR14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r13_re_r13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*', value='aa',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR13.xsd",
        instance="msData/regex/reR13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r12_re_r12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*', value='a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR12.xsd",
        instance="msData/regex/reR12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r9_re_r9_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+',
    value='?0#xd;zzz', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR9.xsd",
        instance="msData/regex/reR9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r8_re_r8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+', value='c?1 abc',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR8.xsd",
        instance="msData/regex/reR8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r3_re_r3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR3.xsd",
        instance="msData/regex/reR3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r2_re_r2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c', value=':', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR2.xsd",
        instance="msData/regex/reR2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_r1_re_r1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c', value='_', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR1.xsd",
        instance="msData/regex/reR1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q22_re_q22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='a\I+\c', value='a 123c',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ22.xsd",
        instance="msData/regex/reQ22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q21_re_q21_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\I*', value='1234',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ21.xsd",
        instance="msData/regex/reQ21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q20_re_q20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\I', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ20.xsd",
        instance="msData/regex/reQ20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q19_re_q19_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\I', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ19.xsd",
        instance="msData/regex/reQ19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q18_re_q18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\I', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ18.xsd",
        instance="msData/regex/reQ18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q17_re_q17_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\I', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ17.xsd",
        instance="msData/regex/reQ17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q12_re_q12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\s\i]*', value='a b c Z :_
    d#xd;y #x9;b #xa;#x20; ', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ12.xsd",
        instance="msData/regex/reQ12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q10_re_q10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c\i*a', value='zabcsdea',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ10.xsd",
        instance="msData/regex/reQ10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q8_re_q8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\i*',
    value='_:abcdefghijklmnopqrstuvwxyzAZ:_', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ8.xsd",
        instance="msData/regex/reQ8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q3_re_q3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\i', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ3.xsd",
        instance="msData/regex/reQ3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q2_re_q2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\i', value=':', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ2.xsd",
        instance="msData/regex/reQ2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_q1_re_q1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\i', value='_', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ1.xsd",
        instance="msData/regex/reQ1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p27_re_p27_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value=' a #xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP27.xsd",
        instance="msData/regex/reP27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p26_re_p26_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value='a b#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP26.xsd",
        instance="msData/regex/reP26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p25_re_p25_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\S*', value='', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP25.xsd",
        instance="msData/regex/reP25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p18_re_p18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\S', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP18.xsd",
        instance="msData/regex/reP18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p13_re_p13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='a a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP13.xsd",
        instance="msData/regex/reP13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p12_re_p12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='a a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP12.xsd",
        instance="msData/regex/reP12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p11_re_p11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='aa',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP11.xsd",
        instance="msData/regex/reP11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p7_re_p7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value='aa
    a', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP7.xsd",
        instance="msData/regex/reP7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p6_re_p6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value='
    #x20;#x9;#xa;#xD;a c#xA;#x9;#xD;#x20;a#x20;#xA;#xD;#x9;
    #x20;#x20;#xD;#xa;', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP6.xsd",
        instance="msData/regex/reP6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p4_re_p4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP4.xsd",
        instance="msData/regex/reP4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p3_re_p3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP3.xsd",
        instance="msData/regex/reP3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p2_re_p2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP2.xsd",
        instance="msData/regex/reP2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_p1_re_p1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\s', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP1.xsd",
        instance="msData/regex/reP1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_o2_re_o2_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='.', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO2.xsd",
        instance="msData/regex/reO2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_o1_re_o1_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='.', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO1.xsd",
        instance="msData/regex/reO1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l88_re_l88_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}+',
    value='#xFFF0;#xFFFD;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL88.xsd",
        instance="msData/regex/reL88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l87_re_l87_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHalfwidthandFullwidthForms}+', value='#xFF00;#xFFEF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL87.xsd",
        instance="msData/regex/reL87.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l85_re_l85_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-B}+', value='#xFE70;#xFEFE;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL85.xsd",
        instance="msData/regex/reL85.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l84_re_l84_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsSmallFormVariants}+',
    value='#xFE50;#xFE6F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL84.xsd",
        instance="msData/regex/reL84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l83_re_l83_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibilityForms}+',
    value='#xFE30;#xFE4F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL83.xsd",
        instance="msData/regex/reL83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l82_re_l82_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCombiningHalfMarks}+',
    value='#xFE20;#xFE2F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL82.xsd",
        instance="msData/regex/reL82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l81_re_l81_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-A}+', value='#xFB50;#xFDFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL81.xsd",
        instance="msData/regex/reL81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l80_re_l80_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsAlphabeticPresentationForms}+', value='#xFB00;#xFB4F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL80.xsd",
        instance="msData/regex/reL80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l79_re_l79_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographs}+', value='#xF900;#xFAFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL79.xsd",
        instance="msData/regex/reL79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l78_re_l78_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}+',
    value='#xE000;#xF8FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL78.xsd",
        instance="msData/regex/reL78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l74_re_l74_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulSyllables}+',
    value='#xAC00;#xD7A3;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL74.xsd",
        instance="msData/regex/reL74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l73_re_l73_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiRadicals}+',
    value='#xA490;#xA4CF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL73.xsd",
        instance="msData/regex/reL73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l72_re_l72_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiSyllables}+',
    value='#xA000;#xA48F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL72.xsd",
        instance="msData/regex/reL72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l71_re_l71_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKUnifiedIdeographs}+',
    value='#x4E00;#x9FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL71.xsd",
        instance="msData/regex/reL71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l70_re_l70_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionA}+',
    value='#x3400;#x4DB5;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL70.xsd",
        instance="msData/regex/reL70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l69_re_l69_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibility}+',
    value='#x3300;#x33FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL69.xsd",
        instance="msData/regex/reL69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l68_re_l68_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsEnclosedCJKLettersandMonths}+', value='#x3200;#x32FF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL68.xsd",
        instance="msData/regex/reL68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l67_re_l67_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofoExtended}+',
    value='#x31A0;#x31BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL67.xsd",
        instance="msData/regex/reL67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l66_re_l66_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsKanbun}+',
    value='#x3190;#x319F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL66.xsd",
        instance="msData/regex/reL66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l65_re_l65_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHangulCompatibilityJamo}+', value='#x3130;#x318F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL65.xsd",
        instance="msData/regex/reL65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l64_re_l64_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofo}+',
    value='#x3100;#x312F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL64.xsd",
        instance="msData/regex/reL64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l63_re_l63_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsKatakana}+',
    value='#x30A0;#x30FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL63.xsd",
        instance="msData/regex/reL63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l62_re_l62_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsHiragana}+',
    value='#x3040;#x309F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL62.xsd",
        instance="msData/regex/reL62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l61_re_l61_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKSymbolsandPunctuation}+', value='#x3000;#x303F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL61.xsd",
        instance="msData/regex/reL61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l60_re_l60_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsIdeographicDescriptionCharacters}+',
    value='#x2FF0;#x2FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL60.xsd",
        instance="msData/regex/reL60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l59_re_l59_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsKangxiRadicals}+',
    value='#x2F00;#x2FDF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL59.xsd",
        instance="msData/regex/reL59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l58_re_l58_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKRadicalsSupplement}+',
    value='#x2E80;#x2EFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL58.xsd",
        instance="msData/regex/reL58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l57_re_l57_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBraillePatterns}+',
    value='#x2800;#x28FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL57.xsd",
        instance="msData/regex/reL57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l56_re_l56_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsDingbats}+',
    value='#x2700;#x27BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL56.xsd",
        instance="msData/regex/reL56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l55_re_l55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousSymbols}+',
    value='#x2600;#x26FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL55.xsd",
        instance="msData/regex/reL55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l54_re_l54_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeometricShapes}+',
    value='#x25A0;#x25FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL54.xsd",
        instance="msData/regex/reL54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l53_re_l53_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBlockElements}+',
    value='#x2580;#x259F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL53.xsd",
        instance="msData/regex/reL53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l52_re_l52_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBoxDrawing}+',
    value='#x2500;#x257F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL52.xsd",
        instance="msData/regex/reL52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l51_re_l51_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsEnclosedAlphanumerics}+',
    value='#x2460;#x24FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL51.xsd",
        instance="msData/regex/reL51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l50_re_l50_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsOpticalCharacterRecognition}+', value='#x2440;#x245F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL50.xsd",
        instance="msData/regex/reL50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l49_re_l49_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsControlPictures}+',
    value='#x2400;#x243F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL49.xsd",
        instance="msData/regex/reL49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l48_re_l48_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousTechnical}+',
    value='#x2300;#x23FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL48.xsd",
        instance="msData/regex/reL48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l47_re_l47_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMathematicalOperators}+',
    value='#x2200;#x22FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL47.xsd",
        instance="msData/regex/reL47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l46_re_l46_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsArrows}+',
    value='#x2190;#x21FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL46.xsd",
        instance="msData/regex/reL46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l45_re_l45_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsNumberForms}+',
    value='#x2150;#x218F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL45.xsd",
        instance="msData/regex/reL45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l44_re_l44_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsLetterlikeSymbols}+',
    value='#x2100;#x214F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL44.xsd",
        instance="msData/regex/reL44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l43_re_l43_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCombiningMarksforSymbols}+', value='#x20D0;#x20FF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL43.xsd",
        instance="msData/regex/reL43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l42_re_l42_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCurrencySymbols}+',
    value='#x20A0;#x20CF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL42.xsd",
        instance="msData/regex/reL42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l41_re_l41_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsSuperscriptsandSubscripts}+', value='#x2070;#x209F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL41.xsd",
        instance="msData/regex/reL41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l40_re_l40_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeneralPunctuation}+',
    value='#x2000;#x206F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL40.xsd",
        instance="msData/regex/reL40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l39_re_l39_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGreekExtended}+',
    value='#x1F00;#x1FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL39.xsd",
        instance="msData/regex/reL39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l38_re_l38_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsLatinExtendedAdditional}+', value='#x1E00;#x1EFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL38.xsd",
        instance="msData/regex/reL38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l37_re_l37_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMongolian}+',
    value='#x1800;#x18AF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL37.xsd",
        instance="msData/regex/reL37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l36_re_l36_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsKhmer}+',
    value='#x1780;#x17FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL36.xsd",
        instance="msData/regex/reL36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l35_re_l35_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsRunic}+',
    value='#x16A0;#x16FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL35.xsd",
        instance="msData/regex/reL35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l34_re_l34_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsOgham}+',
    value='#x1680;#x169F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL34.xsd",
        instance="msData/regex/reL34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l33_re_l33_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsUnifiedCanadianAboriginalSyllabics}+',
    value='#x1400;#x167F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL33.xsd",
        instance="msData/regex/reL33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l32_re_l32_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsCherokee}+',
    value='#x13A0;#x13FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL32.xsd",
        instance="msData/regex/reL32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l31_re_l31_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsEthiopic}+',
    value='#x1200;#x137F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL31.xsd",
        instance="msData/regex/reL31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l30_re_l30_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulJamo}+',
    value='#x1100;#x11FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL30.xsd",
        instance="msData/regex/reL30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l29_re_l29_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeorgian}+',
    value='#x10A0;#x10FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL29.xsd",
        instance="msData/regex/reL29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l28_re_l28_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMyanmar}+',
    value='#x1000;#x109F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL28.xsd",
        instance="msData/regex/reL28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l27_re_l27_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsTibetan}+',
    value='#x0F00;#x0FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL27.xsd",
        instance="msData/regex/reL27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l26_re_l26_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsLao}+',
    value='#x0E80;#x0EFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL26.xsd",
        instance="msData/regex/reL26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l25_re_l25_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsThai}+',
    value='#x0E00;#x0E7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL25.xsd",
        instance="msData/regex/reL25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l24_re_l24_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsSinhala}+',
    value='#x0D80;#x0DFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL24.xsd",
        instance="msData/regex/reL24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l23_re_l23_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsMalayalam}+',
    value='#x0D00;#x0D7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL23.xsd",
        instance="msData/regex/reL23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l22_re_l22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsKannada}+',
    value='#x0C80;#x0CFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL22.xsd",
        instance="msData/regex/reL22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l21_re_l21_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsTelugu}+',
    value='#x0C00;#x0C7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL21.xsd",
        instance="msData/regex/reL21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l20_re_l20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsTamil}+',
    value='#x0B80;#x0BFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL20.xsd",
        instance="msData/regex/reL20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l19_re_l19_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsOriya}+',
    value='#x0B00;#x0B7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL19.xsd",
        instance="msData/regex/reL19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l18_re_l18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGujarati}+',
    value='#x0A80;#x0AFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL18.xsd",
        instance="msData/regex/reL18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l17_re_l17_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsGurmukhi}+',
    value='#x0A00;#x0A7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL17.xsd",
        instance="msData/regex/reL17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l16_re_l16_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBengali}+',
    value='#x0980;#x09FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL16.xsd",
        instance="msData/regex/reL16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l15_re_l15_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsDevanagari}+',
    value='#x0900;#x097F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL15.xsd",
        instance="msData/regex/reL15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l14_re_l14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsThaana}+',
    value='#x0780;#x07BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL14.xsd",
        instance="msData/regex/reL14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l13_re_l13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsSyriac}+',
    value='#x0700;#x074F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL13.xsd",
        instance="msData/regex/reL13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l12_re_l12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsArabic}+',
    value='#x0600;#x06FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL12.xsd",
        instance="msData/regex/reL12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l11_re_l11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsHebrew}+',
    value='#x0590;#x05FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL11.xsd",
        instance="msData/regex/reL11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l10_re_l10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsArmenian}+',
    value='#x0530;#x058F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL10.xsd",
        instance="msData/regex/reL10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l6_re_l6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpacingModifierLetters}+',
    value='#x02B0;#x02FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL6.xsd",
        instance="msData/regex/reL6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l5_re_l5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsIPAExtensions}+',
    value='#x0250;#x02AF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL5.xsd",
        instance="msData/regex/reL5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l4_re_l4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-B}+',
    value='#x0180;#x024F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL4.xsd",
        instance="msData/regex/reL4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l3_re_l3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-A}+',
    value='#x0100;#x017F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL3.xsd",
        instance="msData/regex/reL3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l2_re_l2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatin-1Supplement}+',
    value='#x0080;#x00FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL2.xsd",
        instance="msData/regex/reL2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_l1_re_l1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsBasicLatin}+',
    value='#x9;#xA;#xD;#x20;#x007F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL1.xsd",
        instance="msData/regex/reL1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k88_re_k88_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{IsaA0-a9}', value='',
    type='error', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reK88.xsd",
        instance="msData/regex/reK88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k84_re_k84_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\\p{L}*', value='\a',
    type='valid', RULE='25,26'
    """
    assert_bindings(
        schema="msData/regex/reK84.xsd",
        instance="msData/regex/reK84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k78_re_k78_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Co}*', value='#x2044;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK78.xsd",
        instance="msData/regex/reK78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k76_re_k76_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Cf}*', value='#xE000;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK76.xsd",
        instance="msData/regex/reK76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k74_re_k74_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Cc}*', value='#x070F;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK74.xsd",
        instance="msData/regex/reK74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k72_re_k72_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{C}*', value='#x20A0;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK72.xsd",
        instance="msData/regex/reK72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k70_re_k70_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{So}*', value='#x9;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK70.xsd",
        instance="msData/regex/reK70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k68_re_k68_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Sk}*', value='#x3190;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK68.xsd",
        instance="msData/regex/reK68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k66_re_k66_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Sc}*', value='#x309B;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK66.xsd",
        instance="msData/regex/reK66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k64_re_k64_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Sm}*', value='#x20A0;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK64.xsd",
        instance="msData/regex/reK64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k62_re_k62_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{S}*', value='#x1680;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK62.xsd",
        instance="msData/regex/reK62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k60_re_k60_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Zp}*', value='#x2044;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK60.xsd",
        instance="msData/regex/reK60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k58_re_k58_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Zl}*', value='#x2029;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK58.xsd",
        instance="msData/regex/reK58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k56_re_k56_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Zs}*', value='#x2028;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK56.xsd",
        instance="msData/regex/reK56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k54_re_k54_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Z}*', value='#xBF;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK54.xsd",
        instance="msData/regex/reK54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k52_re_k52_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Po}*', value='#x1680;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK52.xsd",
        instance="msData/regex/reK52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k50_re_k50_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Pf}*', value='#xBF;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK50.xsd",
        instance="msData/regex/reK50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k48_re_k48_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Pi}*', value='#xBB;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK48.xsd",
        instance="msData/regex/reK48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k46_re_k46_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Pe}*', value='#xAB;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK46.xsd",
        instance="msData/regex/reK46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k44_re_k44_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Ps}*', value='#x301E;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK44.xsd",
        instance="msData/regex/reK44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k42_re_k42_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Pd}*', value='#x301D;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK42.xsd",
        instance="msData/regex/reK42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k40_re_k40_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Pc}*', value='#x301C;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK40.xsd",
        instance="msData/regex/reK40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k38_re_k38_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{P}*', value='#xB2;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK38.xsd",
        instance="msData/regex/reK38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k36_re_k36_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{No}*', value='#x203F;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK36.xsd",
        instance="msData/regex/reK36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k34_re_k34_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Nl}*', value='#xB2;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK34.xsd",
        instance="msData/regex/reK34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k32_re_k32_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Nd}*', value='#x1034A;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK32.xsd",
        instance="msData/regex/reK32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k30_re_k30_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{N}*', value='#x903;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK30.xsd",
        instance="msData/regex/reK30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k28_re_k28_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Me}*', value='#xFF10;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK28.xsd",
        instance="msData/regex/reK28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k26_re_k26_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Mc}*', value='#x20DD;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK26.xsd",
        instance="msData/regex/reK26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k24_re_k24_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Mn}*',
    value='#x903;#x1D172;', type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK24.xsd",
        instance="msData/regex/reK24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k22_re_k22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{M}*', value='#x1C5;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK22.xsd",
        instance="msData/regex/reK22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k20_re_k20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Lo}*', value='#x64B;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK20.xsd",
        instance="msData/regex/reK20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k18_re_k18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Lm}*', value='#x5D0;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK18.xsd",
        instance="msData/regex/reK18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k16_re_k16_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Lt}*', value='#x2B0;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK16.xsd",
        instance="msData/regex/reK16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k14_re_k14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Ll}*', value='#x1C5;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK14.xsd",
        instance="msData/regex/reK14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k12_re_k12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{Lu}*', value='#x61;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK12.xsd",
        instance="msData/regex/reK12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k10_re_k10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='#x20DD;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK10.xsd",
        instance="msData/regex/reK10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k4_re_k4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='#$',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK4.xsd",
        instance="msData/regex/reK4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k3_re_k3_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK3.xsd",
        instance="msData/regex/reK3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_k2_re_k2_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='_',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK2.xsd",
        instance="msData/regex/reK2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j73_re_j73_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Cc}*', value='#x9;',
    type='valid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ73.xsd",
        instance="msData/regex/reJ73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j67_re_j67_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Sk}*',
    value='#x309B;#xFFE3;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ67.xsd",
        instance="msData/regex/reJ67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j65_re_j65_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Sc}*',
    value='#x20A0;#xFFE6;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ65.xsd",
        instance="msData/regex/reJ65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j63_re_j63_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Sm}*',
    value='#x2044;#xFFE2;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ63.xsd",
        instance="msData/regex/reJ63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j59_re_j59_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Zp}*', value='#x2029;',
    type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ59.xsd",
        instance="msData/regex/reJ59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j57_re_j57_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Zl}*', value='#x2028;',
    type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ57.xsd",
        instance="msData/regex/reJ57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j55_re_j55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Zs}*',
    value='#x1680;#x3000;', type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ55.xsd",
        instance="msData/regex/reJ55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j53_re_j53_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Z}*',
    value='#x1680;#x3000;#x2028;#x2028;#x2029;#x2029;', type='valid',
    RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ53.xsd",
        instance="msData/regex/reJ53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j51_re_j51_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Po}*', value='#xBF;#xFF64;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ51.xsd",
        instance="msData/regex/reJ51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j49_re_j49_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Pf}*', value='#xBB;#x203A;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ49.xsd",
        instance="msData/regex/reJ49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j47_re_j47_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Pi}*', value='#xAB;#x2039;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ47.xsd",
        instance="msData/regex/reJ47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j45_re_j45_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Pe}*',
    value='#x301E;#xFF63;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ45.xsd",
        instance="msData/regex/reJ45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j43_re_j43_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Ps}*',
    value='#x301D;#xFF62;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ43.xsd",
        instance="msData/regex/reJ43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j41_re_j41_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Pd}*',
    value='#x301C;#xFF0D;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ41.xsd",
        instance="msData/regex/reJ41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j37_re_j37_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{P}*', value='#x203F;#xFF65;#
    x301C;#x301C;#xFF0D;#x301D;#x301D;#xFF62;#x301E;#x301E;#xFF63;#xAB;#xA
    B;#x2039;#xBB;#xBB;#x203A;#xBF;#xBF;#xFF64;', type='valid',
    RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ37.xsd",
        instance="msData/regex/reJ37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j27_re_j27_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Me}*',
    value='#x20DD;#x20E0;', type='valid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ27.xsd",
        instance="msData/regex/reJ27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j17_re_j17_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Lm}*',
    value='#x2B0;#xFF9F;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ17.xsd",
        instance="msData/regex/reJ17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j15_re_j15_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\p{Lt}*',
    value='#x1C5;#x1FFC;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ15.xsd",
        instance="msData/regex/reJ15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_j4_re_j4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\p{L}*]{0,2}', value='aX',
    type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ4.xsd",
        instance="msData/regex/reJ4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i83_re_i83_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',pattern="\\.*,\\s*,\\S*,\\i*,\\I?,\\c+,\\
    C+,\\d{0,3},\\D{1,1000},\\w*,\\W*",
    value='\.,\s,\S,\i,\I,\c,\C,\d,\D,\w,\W', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI83.xsd",
        instance="msData/regex/reI83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i82_re_i82_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern="\\.,\\s,\\S,\\i,\\I,\\c,\\C,\\d,\\D,\\w,\\W",
    value='\.,\s,\S,\i,\I,\c,\C,\d,\D,\w,\W', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI82.xsd",
        instance="msData/regex/reI82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i78_re_i78_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\c', value='\c', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI78.xsd",
        instance="msData/regex/reI78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i77_re_i77_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI77.xsd",
        instance="msData/regex/reI77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i74_re_i74_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b ', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI74.xsd",
        instance="msData/regex/reI74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i73_re_i73_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI73.xsd",
        instance="msData/regex/reI73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i72_re_i72_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI72.xsd",
        instance="msData/regex/reI72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i71_re_i71_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\na\nb\nc\n', value=' a b c ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI71.xsd",
        instance="msData/regex/reI71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i69_re_i69_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\ta\tb\tc\t', value=' a b c ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI69.xsd",
        instance="msData/regex/reI69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i67_re_i67_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\n\ra\n\rb', value=' a b',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI67.xsd",
        instance="msData/regex/reI67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i65_re_i65_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='a\r\nb', value='a b',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI65.xsd",
        instance="msData/regex/reI65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i55_re_i55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a b ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI55.xsd",
        instance="msData/regex/reI55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i45_re_i45_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\]', value=']', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI45.xsd",
        instance="msData/regex/reI45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i44_re_i44_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\[', value='[', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI44.xsd",
        instance="msData/regex/reI44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i43_re_i43_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\)', value=')', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI43.xsd",
        instance="msData/regex/reI43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i42_re_i42_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\(', value='(', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI42.xsd",
        instance="msData/regex/reI42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i41_re_i41_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\}', value='}', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI41.xsd",
        instance="msData/regex/reI41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i40_re_i40_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\{', value='{', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI40.xsd",
        instance="msData/regex/reI40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i39_re_i39_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\+', value='+', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI39.xsd",
        instance="msData/regex/reI39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i38_re_i38_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\*', value='*', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI38.xsd",
        instance="msData/regex/reI38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i37_re_i37_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\?', value='?', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI37.xsd",
        instance="msData/regex/reI37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i36_re_i36_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\^', value='^', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI36.xsd",
        instance="msData/regex/reI36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i35_re_i35_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\-', value='-', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI35.xsd",
        instance="msData/regex/reI35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i34_re_i34_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\.', value='.', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI34.xsd",
        instance="msData/regex/reI34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i33_re_i33_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\|', value='|', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI33.xsd",
        instance="msData/regex/reI33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i32_re_i32_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\', value='\', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI32.xsd",
        instance="msData/regex/reI32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i31_re_i31_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\t', value='#x9;',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI31.xsd",
        instance="msData/regex/reI31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i29_re_i29_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\n', value='#xA;',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI29.xsd",
        instance="msData/regex/reI29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i25_re_i25_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\r', value='\r', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI25.xsd",
        instance="msData/regex/reI25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i21_re_i21_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\n', value='\n', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI21.xsd",
        instance="msData/regex/reI21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i17_re_i17_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\\t', value='\t', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI17.xsd",
        instance="msData/regex/reI17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i16_re_i16_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='aa?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI16.xsd",
        instance="msData/regex/reI16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i15_re_i15_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a??',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI15.xsd",
        instance="msData/regex/reI15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i14_re_i14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI14.xsd",
        instance="msData/regex/reI14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i13_re_i13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a?a?a?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI13.xsd",
        instance="msData/regex/reI13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i12_re_i12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI12.xsd",
        instance="msData/regex/reI12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i10_re_i10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='a',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI10.xsd",
        instance="msData/regex/reI10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i9_re_i9_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='aa*',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI9.xsd",
        instance="msData/regex/reI9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i8_re_i8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='a**',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI8.xsd",
        instance="msData/regex/reI8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_i1_re_i1_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(\n\r\t\\\|\.\-\^\?\*\+\{\}\[\]\(\))*',
    value='\|.-^?*+[]{}()*[[]{}}))#xA;#xD;#x9;#x9;#xA;#xa;#xd;*()',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI1.xsd",
        instance="msData/regex/reI1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h19_re_h19_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-a-x-x]+', value='a-x',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH19.xsd",
        instance="msData/regex/reH19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h18_re_h18_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-]*', value='a--aa---',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH18.xsd",
        instance="msData/regex/reH18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h17_re_h17_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[-a]+', value='a--aa---',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH17.xsd",
        instance="msData/regex/reH17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h16_re_h16_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[-]', value='-', type='valid',
    RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH16.xsd",
        instance="msData/regex/reH16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h12_re_h12_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[][',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH12.xsd",
        instance="msData/regex/reH12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h11_re_h11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\]\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH11.xsd",
        instance="msData/regex/reH11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h10_re_h10_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[\\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH10.xsd",
        instance="msData/regex/reH10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h9_re_h9_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[]',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH9.xsd",
        instance="msData/regex/reH9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h8_re_h8_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\[]',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH8.xsd",
        instance="msData/regex/reH8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h7_re_h7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\[',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH7.xsd",
        instance="msData/regex/reH7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h6_re_h6_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value=']',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH6.xsd",
        instance="msData/regex/reH6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h5_re_h5_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH5.xsd",
        instance="msData/regex/reH5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_h4_re_h4_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH4.xsd",
        instance="msData/regex/reH4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g50_re_g50_i(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[#x10000;]', value='#x10000;',
    type='valid', RULE='19' MK & HST agreed this one is OK, as does MS's
    own comment
    """
    assert_bindings(
        schema="msData/regex/reG50.xsd",
        instance="msData/regex/reG50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g49_re_g49_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[?]', value='#x0FFF;',
    type='valid', RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG49.xsd",
        instance="msData/regex/reG49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g47_re_g47_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[@]', value='@', type='valid',
    RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG47.xsd",
        instance="msData/regex/reG47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g44_re_g44_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[=->]', value='>',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG44.xsd",
        instance="msData/regex/reG44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g43_re_g43_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[=->]', value='=',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG43.xsd",
        instance="msData/regex/reG43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g38_re_g38_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[1-\]]+', value='1]',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG38.xsd",
        instance="msData/regex/reG38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g36_re_g36_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\*a]*', value='a*a****aaaaa*',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG36.xsd",
        instance="msData/regex/reG36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g33_re_g33_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG33.xsd",
        instance="msData/regex/reG33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g32_re_g32_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG32.xsd",
        instance="msData/regex/reG32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g31_re_g31_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1z8', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG31.xsd",
        instance="msData/regex/reG31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g30_re_g30_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a1z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG30.xsd",
        instance="msData/regex/reG30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g29_re_g29_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1z-8a-1z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG29.xsd",
        instance="msData/regex/reG29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g28_re_g28_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='c-4z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG28.xsd",
        instance="msData/regex/reG28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g27_re_g27_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1x-7', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG27.xsd",
        instance="msData/regex/reG27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g26_re_g26_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*', value='',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG26.xsd",
        instance="msData/regex/reG26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g22_re_g22_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG22.xsd",
        instance="msData/regex/reG22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g20_re_g20_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?c?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG20.xsd",
        instance="msData/regex/reG20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g19_re_g19_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?b?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG19.xsd",
        instance="msData/regex/reG19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g18_re_g18_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?a?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG18.xsd",
        instance="msData/regex/reG18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g14_re_g14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='[\\\|\.\?\*\+\(\)\{\}\-\[\]\^]*', value='\|.?*+(){}-[]^',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG14.xsd",
        instance="msData/regex/reG14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g13_re_g13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\t]', value='#x9;',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG13.xsd",
        instance="msData/regex/reG13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g11_re_g11_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[\n]', value='#xA;',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG11.xsd",
        instance="msData/regex/reG11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g8_re_g8_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[0-z]*',
    value='1234567890:;<=>?@Azaz', type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG8.xsd",
        instance="msData/regex/reG8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g6_re_g6_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-a]', value='a',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG6.xsd",
        instance="msData/regex/reG6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_g4_re_g4_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[1-3]{1,4}', value='123',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG4.xsd",
        instance="msData/regex/reG4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f55_re_f55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[a-\}-]', value='}-',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF55.xsd",
        instance="msData/regex/reF55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f54_re_f54_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[a-abc]', value='abc',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF54.xsd",
        instance="msData/regex/reF54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f46_re_f46_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a*a',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF46.xsd",
        instance="msData/regex/reF46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f45_re_f45_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(^\?)*', value='a+*abc',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF45.xsd",
        instance="msData/regex/reF45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f43_re_f43_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='^\P{IsBasicLatin}', value='a',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF43.xsd",
        instance="msData/regex/reF43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f40_re_f40_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='^\p{IsBasicLatin}',
    value='#x0100;', type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF40.xsd",
        instance="msData/regex/reF40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f32_re_f32_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[a-\}]+', value='abcxyz}',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF32.xsd",
        instance="msData/regex/reF32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f12_re_f12_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value=' a',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF12.xsd",
        instance="msData/regex/reF12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f11_re_f11_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='ab',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF11.xsd",
        instance="msData/regex/reF11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f10_re_f10_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='a',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF10.xsd",
        instance="msData/regex/reF10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f9_re_f9_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF9.xsd",
        instance="msData/regex/reF9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f7_re_f7_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='[^\s]{3}', value='abc',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF7.xsd",
        instance="msData/regex/reF7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_f4_re_f4_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='[^2-9a-x]{2}', value='1z',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF4.xsd",
        instance="msData/regex/reF4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_e14_re_e14_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string',
    pattern='(([\.\\\?\*\+\{\}\[\]\(\)\|]?)*)+',
    value='.\?*+{}[]()|.\?*+{}[]()|.\?*+{}[]()|', type='valid', RULE='10'
    """
    assert_bindings(
        schema="msData/regex/reE14.xsd",
        instance="msData/regex/reE14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_e13_re_e13_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='\.\\\?\*\+\{\}\[\]\(\)\|',
    value='.\?*+{}[]()|', type='valid', RULE='10'
    """
    assert_bindings(
        schema="msData/regex/reE13.xsd",
        instance="msData/regex/reE13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_e10_re_e10_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='|', value='', type='error',
    RULE='10'. This is valid because branch allow zero or more pieces. A
    single '|' will be same ase EMPTY, it will not allow anything.
    """
    assert_bindings(
        schema="msData/regex/reE10.xsd",
        instance="msData/regex/reE10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d6_re_d6_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xxwoman1ygirl1xymanyboy0xxwoman1ygirl1xymany',
    type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD6.xsd",
        instance="msData/regex/reD6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d5_re_d5_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xxwoman1ygirl1xymany', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD5.xsd",
        instance="msData/regex/reD5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d4_re_d4_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='girl1xymany', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD4.xsd",
        instance="msData/regex/reD4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d3_re_d3_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='woman1y', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD3.xsd",
        instance="msData/regex/reD3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d2_re_d2_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xx', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD2.xsd",
        instance="msData/regex/reD2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_d1_re_d1_v(mode, save_output, output_format):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD1.xsd",
        instance="msData/regex/reD1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c78_re_c78_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='bbccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC78.xsd",
        instance="msData/regex/reC78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c77_re_c77_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='bbcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC77.xsd",
        instance="msData/regex/reC77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c76_re_c76_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC76.xsd",
        instance="msData/regex/reC76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c75_re_c75_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC75.xsd",
        instance="msData/regex/reC75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c74_re_c74_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC74.xsd",
        instance="msData/regex/reC74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c73_re_c73_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC73.xsd",
        instance="msData/regex/reC73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c70_re_c70_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab{0,0}', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC70.xsd",
        instance="msData/regex/reC70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c58_re_c58_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='abababababababa
    bababababababababababababababababababababababababab', type='valid',
    RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC58.xsd",
        instance="msData/regex/reC58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c57_re_c57_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ababab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC57.xsd",
        instance="msData/regex/reC57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c56_re_c56_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='abab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC56.xsd",
        instance="msData/regex/reC56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c51_re_c51_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a ba b',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC51.xsd",
        instance="msData/regex/reC51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c50_re_c50_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a b',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC50.xsd",
        instance="msData/regex/reC50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c49_re_c49_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC49.xsd",
        instance="msData/regex/reC49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c43_re_c43_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abacac', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC43.xsd",
        instance="msData/regex/reC43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c42_re_c42_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abac', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC42.xsd",
        instance="msData/regex/reC42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c41_re_c41_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?', value='ab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC41.xsd",
        instance="msData/regex/reC41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c35_re_c35_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bbbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC35.xsd",
        instance="msData/regex/reC35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c34_re_c34_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC34.xsd",
        instance="msData/regex/reC34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c33_re_c33_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC33.xsd",
        instance="msData/regex/reC33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c32_re_c32_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='aaabbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC32.xsd",
        instance="msData/regex/reC32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c28_re_c28_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc{2}', value='abcc',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC28.xsd",
        instance="msData/regex/reC28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c22_re_c22_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='abbc',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC22.xsd",
        instance="msData/regex/reC22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c18_re_c18_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC18.xsd",
        instance="msData/regex/reC18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c17_re_c17_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC17.xsd",
        instance="msData/regex/reC17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c16_re_c16_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC16.xsd",
        instance="msData/regex/reC16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c11_re_c11_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})+',
    value='aaaaaaaaaaaaaaaaaaaa', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC11.xsd",
        instance="msData/regex/reC11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c10_re_c10_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='aaaa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC10.xsd",
        instance="msData/regex/reC10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c9_re_c9_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='aa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC9.xsd",
        instance="msData/regex/reC9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c4_re_c4_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC4.xsd",
        instance="msData/regex/reC4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c3_re_c3_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='abab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC3.xsd",
        instance="msData/regex/reC3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_c2_re_c2_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0}', value='', type='valid',
    RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC2.xsd",
        instance="msData/regex/reC2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b78_re_b78_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a{0}', value='', type='valid',
    RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB78.xsd",
        instance="msData/regex/reB78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b57_re_b57_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??',
    value='abbbbca?', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB57.xsd",
        instance="msData/regex/reB57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b56_re_b56_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abca??',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB56.xsd",
        instance="msData/regex/reB56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b55_re_b55_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??',
    value='abbbc??', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB55.xsd",
        instance="msData/regex/reB55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b54_re_b54_v(mode, save_output, output_format):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abc?',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB54.xsd",
        instance="msData/regex/reB54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b48_re_b48_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='abbbc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB48.xsd",
        instance="msData/regex/reB48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b47_re_b47_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB47.xsd",
        instance="msData/regex/reB47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b46_re_b46_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='bcccccc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB46.xsd",
        instance="msData/regex/reB46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b45_re_b45_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB45.xsd",
        instance="msData/regex/reB45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b44_re_b44_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='b',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB44.xsd",
        instance="msData/regex/reB44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b39_re_b39_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc*', value='abccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccc', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB39.xsd",
        instance="msData/regex/reB39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b38_re_b38_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc*', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB38.xsd",
        instance="msData/regex/reB38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b37_re_b37_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc*', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB37.xsd",
        instance="msData/regex/reB37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b30_re_b30_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab*c', value='ac',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB30.xsd",
        instance="msData/regex/reB30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b29_re_b29_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab*c', value='abbbbbbbc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB29.xsd",
        instance="msData/regex/reB29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b28_re_b28_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab*c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB28.xsd",
        instance="msData/regex/reB28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b24_re_b24_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc+', value='abccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccc', type='valid',
    RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB24.xsd",
        instance="msData/regex/reB24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b23_re_b23_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc+', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB23.xsd",
        instance="msData/regex/reB23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b18_re_b18_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab+c', value='abbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbc', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB18.xsd",
        instance="msData/regex/reB18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b17_re_b17_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab+c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB17.xsd",
        instance="msData/regex/reB17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b12_re_b12_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc?', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB12.xsd",
        instance="msData/regex/reB12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b11_re_b11_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='abc?', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB11.xsd",
        instance="msData/regex/reB11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b2_re_b2_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab?c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB2.xsd",
        instance="msData/regex/reB2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_b1_re_b1_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab?c', value='ac',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB1.xsd",
        instance="msData/regex/reB1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a45_re_a45_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern=' a|b ', value='a',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA45.xsd",
        instance="msData/regex/reA45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a31_re_a31_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='d',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA31.xsd",
        instance="msData/regex/reA31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a30_re_a30_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='c',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA30.xsd",
        instance="msData/regex/reA30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a29_re_a29_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='b',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA29.xsd",
        instance="msData/regex/reA29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a28_re_a28_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='a',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA28.xsd",
        instance="msData/regex/reA28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a24_re_a24_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='ab', value='ab', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA24.xsd",
        instance="msData/regex/reA24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a17_re_a17_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b', value='b', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA17.xsd",
        instance="msData/regex/reA17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a16_re_a16_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|b', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA16.xsd",
        instance="msData/regex/reA16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a12_re_a12_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a|a', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA12.xsd",
        instance="msData/regex/reA12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a8_re_a8_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='a', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA8.xsd",
        instance="msData/regex/reA8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a7_re_a7_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='', value='', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA7.xsd",
        instance="msData/regex/reA7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_re_a1_re_a1_v(mode, save_output, output_format):
    """
    TEST :branch : base='string', pattern='', value='', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA1.xsd",
        instance="msData/regex/reA1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_t10_sch_t10_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with an
    attributeGroup, attribute group's content items are a subset of the
    redefined group, test that attribute uses are not inherited. base
    attriburte with effective value absent, but redefining attribute has
    fixed="bar" , (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT10_a.xsd",
        instance="msData/schema/schT10.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_t9_sch_t9_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with a
    attributeGroup, attribute group's content items are a subset of the
    redefined group, test that attribute uses are not inherited. Have a
    default="foo" in redefined attriubte, but redefining attribute has
    default="bar", the actual value of the instance should have 'bar' as
    the default attribute value (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT9_a.xsd",
        instance="msData/schema/schT9.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_t3_sch_t3_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with a
    attributeGroup, attribute group's content items are a subset of the
    redefined group, (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT3_a.xsd",
        instance="msData/schema/schT3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_q3_sch_q3_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has a restriction, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schQ3_a.xsd",
        instance="msData/schema/schQ3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_q1_sch_q1_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has an extension, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schQ1_a.xsd",
        instance="msData/schema/schQ1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_p2_sch_p2_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has a restriction, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schP2_a.xsd",
        instance="msData/schema/schP2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g12_sch_g12_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="B", All declaration in B and C should
    be available to validation
    """
    assert_bindings(
        schema="msData/schema/schG12_a.xsd",
        instance="msData/schema/schG12.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g8_sch_g8_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B and C, B is
    bogus URL, C is valid XSD, test that there is no error and C is
    imported.
    """
    assert_bindings(
        schema="msData/schema/schG8_a.xsd",
        instance="msData/schema/schG8.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g7_sch_g7_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A imports B and B and C,
    B imports C and D, C imports D and A, multiple import of the same XSD
    is ok
    """
    assert_bindings(
        schema="msData/schema/schG7_a.xsd",
        instance="msData/schema/schG7.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g5_sch_g5_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B and C, A's
    ns="A", B's ns="B", C's ns="B", (B and C have no confilcting decl)
    """
    assert_bindings(
        schema="msData/schema/schG5_a.xsd",
        instance="msData/schema/schG5.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g4_sch_g4_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B and C, A's
    ns="A", B's ns="B", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG4_a.xsd",
        instance="msData/schema/schG4.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g3_sch_g3_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="A", (A and C have no confilcting decl)
    """
    assert_bindings(
        schema="msData/schema/schG3_a.xsd",
        instance="msData/schema/schG3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g2_sch_g2_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG2_a.xsd",
        instance="msData/schema/schG2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_g1_sch_g1_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG1_a.xsd",
        instance="msData/schema/schG1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_f5_sch_f5_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="A", Y's ns="B", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF5_a.xsd",
        instance="msData/schema/schF5.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_f2_sch_f2_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="", Y's ns="A", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF2_a.xsd",
        instance="msData/schema/schF2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_f1_sch_f1_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="A", Y's ns="", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF1_a.xsd",
        instance="msData/schema/schF1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_e4_sch_e4_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : import namespace="foo"
    """
    assert_bindings(
        schema="msData/schema/schE4.xsd",
        instance="msData/schema/schE4.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_d10_sch_d10_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : validate instance
    against 'chameleon' include schema (2)
    """
    assert_bindings(
        schema="msData/schema/schD10_a.xsd",
        instance="msData/schema/schD10.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_d7_sch_d7_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A includes B and C, B is
    bogus URL, C is valid XSD, test that there is no error and C is
    included.
    """
    assert_bindings(
        schema="msData/schema/schD7_a.xsd",
        instance="msData/schema/schD7.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="namespaces",
    )


def test_sch_d5_sch_d5_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : A include B and C, A's
    ns="A", B's ns="A", C's ns="A", type ref from A to B and C, B to A and
    C, C to A and B
    """
    assert_bindings(
        schema="msData/schema/schD5_a.xsd",
        instance="msData/schema/schD5.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="namespaces",
    )


def test_sch_c4_sch_c4_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : XSD A include XSD B, A's
    ns="A", B's ns="A", test the namespace of include (4.2.1) (SRC 2)
    """
    assert_bindings(
        schema="msData/schema/schC4_a.xsd",
        instance="msData/schema/schC4.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_c3_sch_c3_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : XSD A include XSD B, A's
    ns="", B's ns="", test the namespace of include (4.2.1) (SRC 2)
    """
    assert_bindings(
        schema="msData/schema/schC3_a.xsd",
        instance="msData/schema/schC3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_a3_sch_a3_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd), SchemaLocation:, NoNSSchemaLocation:,
    """
    assert_bindings(
        schema="msData/schema/schA3_a.xsd",
        instance="msData/schema/schA3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sch_a1_sch_a1_v(mode, save_output, output_format):
    """
    TEST :schema collection and schema location : Schema Collection:
    (A,a.xsd), SchemaLocation: (B,b.xsd), NoNSSchemaLocation: c.xsd
    """
    assert_bindings(
        schema="msData/schema/schA1_a.xsd",
        instance="msData/schema/schA1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z075_st_z075_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: xs:NOTATION
    type on elements
    """
    assert_bindings(
        schema="msData/simpleType/stZ075.xsd",
        instance="msData/simpleType/stZ075.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z074_st_z074_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : chameleon lists and
    union of lists
    """
    assert_bindings(
        schema="msData/simpleType/stZ074_a.xsd",
        instance="msData/simpleType/stZ074.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z072_st_z072_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: valid default
    value of a list of union with enumeration facet
    """
    assert_bindings(
        schema="msData/simpleType/stZ072.xsd",
        instance="msData/simpleType/stZ072.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z071_st_z071_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : adding chameleon
    schemas that have unions without memberTypes
    """
    assert_bindings(
        schema="msData/simpleType/test298668_a.xsd",
        instance="msData/simpleType/test298668.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z057_st_z057_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anyType as a valid data type for the head element of a substitution
    group
    """
    assert_bindings(
        schema="msData/simpleType/test107331_j.xsd",
        instance="msData/simpleType/test107331_10.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


@pytest.mark.skip(reason="Invalid definition")
def test_st_z055_st_z055_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (CT with simplecontent)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_e.xsd",
        instance="msData/simpleType/test107331_9.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z054_st_z054_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (List Unions)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_c.xsd",
        instance="msData/simpleType/test107331_8.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z053_st_z053_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (anyType)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_h.xsd",
        instance="msData/simpleType/test107331_7.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z052_st_z052_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (basic types)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_a.xsd",
        instance="msData/simpleType/test107331_6.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z050_st_z050_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, anySimpleType substituting anyType
    """
    assert_bindings(
        schema="msData/simpleType/test107331_h.xsd",
        instance="msData/simpleType/test107331_5.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


@pytest.mark.skip(reason="Invalid definition")
def test_st_z047_st_z047_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, CT with simpleContent
    """
    assert_bindings(
        schema="msData/simpleType/test107331_e.xsd",
        instance="msData/simpleType/test107331_4.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z046_st_z046_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, substituting anyST with anyST
    """
    assert_bindings(
        schema="msData/simpleType/test107331_d.xsd",
        instance="msData/simpleType/test107331_3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z045_st_z045_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, Lists and Unions
    """
    assert_bindings(
        schema="msData/simpleType/test107331_c.xsd",
        instance="msData/simpleType/test107331_2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z043_st_z043_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group.
    """
    assert_bindings(
        schema="msData/simpleType/test107331_a.xsd",
        instance="msData/simpleType/test107331_1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z040_st_z040_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Using an xsd union
    in the definition of another
    """
    assert_bindings(
        schema="msData/simpleType/stZ040.xsd",
        instance="msData/simpleType/stZ040.xml",
        class_name="Info2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z036_st_z036_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: simpleType
    restriction with pattern should be the intersaction of the base type
    and the derived type.
    """
    assert_bindings(
        schema="msData/simpleType/stZ035.xsd",
        instance="msData/simpleType/stZ036.xml",
        class_name="A",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z031_st_z031_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: we should not
    parser Name as QName.
    """
    assert_bindings(
        schema="msData/simpleType/stZ031.xsd",
        instance="msData/simpleType/stZ031.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z030_st_z030_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: facet
    minExclusive in restricted type while minInclusive is in base type
    """
    assert_bindings(
        schema="msData/simpleType/stZ030.xsd",
        instance="msData/simpleType/stZ030.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z015_st_z015_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : The value of
    totalDigits facet on a base simple type carrying forward to the
    derivedType
    """
    assert_bindings(
        schema="msData/simpleType/stZ015.xsd",
        instance="msData/simpleType/stZ015.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z008_st_z008_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : rename a
    complexType to anySimpleType using extension, and extend it to another
    complexType with attribute
    """
    assert_bindings(
        schema="msData/simpleType/stZ008.xsd",
        instance="msData/simpleType/stZ008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z007_st_z007_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : rename a
    complexType to anySimpleType using extension, and restrict it to
    another complexType
    """
    assert_bindings(
        schema="msData/simpleType/stZ007.xsd",
        instance="msData/simpleType/stZ007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_z004_st_z004_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd:can not specify
    HalfWidth-KANA to Instance documents when schema has pattern facet
    including Japanese character.
    """
    assert_bindings(
        schema="msData/simpleType/stZ004.xsd",
        instance="msData/simpleType/stZ004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_h007_st_h007_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of states with restriction facet 'enumeration' with a value of
    'CA' instance document has state = 'CA'
    """
    assert_bindings(
        schema="msData/simpleType/stH007.xsd",
        instance="msData/simpleType/stH007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_h005_st_h005_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of zip codes with restriction facet 'pattern' with a value of
    '[0-8]{5}' instance document has zip code='12345'
    """
    assert_bindings(
        schema="msData/simpleType/stH005.xsd",
        instance="msData/simpleType/stH005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_h003_st_h003_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union with memberTypes of a list of states(restricted strings) and a
    list of zip codes(restricted positiveIntegers) instance document has
    valid values
    """
    assert_bindings(
        schema="msData/simpleType/stH003.xsd",
        instance="msData/simpleType/stH003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_h001_st_h001_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union of positiveInteger with minInclusive and maxInclusive
    restrictions and NMTOKEN with enumeration instance document has valid
    values
    """
    assert_bindings(
        schema="msData/simpleType/stH001.xsd",
        instance="msData/simpleType/stH001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g012_st_g012_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of string type
    with facet of 'pattern' value = '[A-C]{0,2}' instance document has
    'CA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG012.xsd",
        instance="msData/simpleType/stG012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g010_st_g010_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of NMTOKEN
    type with facet of 'enumeration' value = 'CA' instance document has
    'CA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG010.xsd",
        instance="msData/simpleType/stG010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g008_st_g008_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'minLength' value = '2' instance document has 3 items
    """
    assert_bindings(
        schema="msData/simpleType/stG008.xsd",
        instance="msData/simpleType/stG008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g006_st_g006_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'length' value = '2' instance document has 2 items
    """
    assert_bindings(
        schema="msData/simpleType/stG006.xsd",
        instance="msData/simpleType/stG006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g004_st_g004_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : schema is a list
    derived from a union of integer and NMTOKEN instance document contains
    valid items of integer and NMTOKEN
    """
    assert_bindings(
        schema="msData/simpleType/stG004.xsd",
        instance="msData/simpleType/stG004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g002_st_g002_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'maxLength' value = '3' instance document has 3 items
    """
    assert_bindings(
        schema="msData/simpleType/stG002.xsd",
        instance="msData/simpleType/stG002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_g001_st_g001_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    instance document contains items of the same atomic type
    """
    assert_bindings(
        schema="msData/simpleType/stG001.xsd",
        instance="msData/simpleType/stG001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ste099_ste099_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (45)
    """
    assert_bindings(
        schema="msData/simpleType/ste099.xsd",
        instance="msData/simpleType/ste099.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e096_st_e096_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (42)
    """
    assert_bindings(
        schema="msData/simpleType/stE096.xsd",
        instance="msData/simpleType/stE096.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e094_st_e094_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (40)
    """
    assert_bindings(
        schema="msData/simpleType/stE094.xsd",
        instance="msData/simpleType/stE094.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e093_st_e093_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (39)
    """
    assert_bindings(
        schema="msData/simpleType/stE093.xsd",
        instance="msData/simpleType/stE093.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e092_st_e092_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (38)
    """
    assert_bindings(
        schema="msData/simpleType/stE092.xsd",
        instance="msData/simpleType/stE092.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e091_st_e091_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (37)
    """
    assert_bindings(
        schema="msData/simpleType/stE091.xsd",
        instance="msData/simpleType/stE091.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e090_st_e090_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (36)
    """
    assert_bindings(
        schema="msData/simpleType/stE090.xsd",
        instance="msData/simpleType/stE090.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e081_st_e081_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (34)
    """
    assert_bindings(
        schema="msData/simpleType/stE081.xsd",
        instance="msData/simpleType/stE081.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e080_st_e080_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (33)
    """
    assert_bindings(
        schema="msData/simpleType/stE080.xsd",
        instance="msData/simpleType/stE080.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e079_st_e079_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (32)
    """
    assert_bindings(
        schema="msData/simpleType/stE079.xsd",
        instance="msData/simpleType/stE079.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e077_st_e077_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (30)
    """
    assert_bindings(
        schema="msData/simpleType/stE077.xsd",
        instance="msData/simpleType/stE077.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_ste074v_ste074v_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (27)
    """
    assert_bindings(
        schema="msData/simpleType/ste074v.xsd",
        instance="msData/simpleType/ste074v.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e073v_st_e073v_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (25)
    """
    assert_bindings(
        schema="msData/simpleType/stE073v.xsd",
        instance="msData/simpleType/stE073v.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e072_st_e072_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (23) Changed to add a wrapper element to avoid problems with
    having an ID in the outermost element - MHK 2010-07-10 But schema is
    possibly invalid in XSD 1.0 because ID cannot have a fixed value.
    """
    assert_bindings(
        schema="msData/simpleType/stE072.xsd",
        instance="msData/simpleType/stE072.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e069_st_e069_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (20)
    """
    assert_bindings(
        schema="msData/simpleType/stE069.xsd",
        instance="msData/simpleType/stE069.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e068_st_e068_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (19)
    """
    assert_bindings(
        schema="msData/simpleType/stE068.xsd",
        instance="msData/simpleType/stE068.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e067_st_e067_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (18)
    """
    assert_bindings(
        schema="msData/simpleType/stE067.xsd",
        instance="msData/simpleType/stE067.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e066_st_e066_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (17)
    """
    assert_bindings(
        schema="msData/simpleType/stE066.xsd",
        instance="msData/simpleType/stE066.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e065_st_e065_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (16)
    """
    assert_bindings(
        schema="msData/simpleType/stE065.xsd",
        instance="msData/simpleType/stE065.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e064_st_e064_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (15)
    """
    assert_bindings(
        schema="msData/simpleType/stE064.xsd",
        instance="msData/simpleType/stE064.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e062_st_e062_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (13)
    """
    assert_bindings(
        schema="msData/simpleType/stE062.xsd",
        instance="msData/simpleType/stE062.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e061_st_e061_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (12)
    """
    assert_bindings(
        schema="msData/simpleType/stE061.xsd",
        instance="msData/simpleType/stE061.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e060_st_e060_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (11)
    """
    assert_bindings(
        schema="msData/simpleType/stE060.xsd",
        instance="msData/simpleType/stE060.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e059_st_e059_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (10)
    """
    assert_bindings(
        schema="msData/simpleType/stE059.xsd",
        instance="msData/simpleType/stE059.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e058_st_e058_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (9)
    """
    assert_bindings(
        schema="msData/simpleType/stE058.xsd",
        instance="msData/simpleType/stE058.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e057_st_e057_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (8)
    """
    assert_bindings(
        schema="msData/simpleType/stE057.xsd",
        instance="msData/simpleType/stE057.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e055_st_e055_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (6)
    """
    assert_bindings(
        schema="msData/simpleType/stE055.xsd",
        instance="msData/simpleType/stE055.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e052_st_e052_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (3)
    """
    assert_bindings(
        schema="msData/simpleType/stE052.xsd",
        instance="msData/simpleType/stE052.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_st_e050_st_e050_v(mode, save_output, output_format):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (1)
    """
    assert_bindings(
        schema="msData/simpleType/stE050.xsd",
        instance="msData/simpleType/stE050.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z013c_wild_z013c_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873c.xml",
        class_name="Sub3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z013b_wild_z013b_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873b.xml",
        class_name="Sub2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z007_wild_z007_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : XSD: When processContents=lax, xsd:any
    doesn't allow attributes from target namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildZ007.xsd",
        instance="msData/wildcards/wildZ007.xml",
        class_name="Stylesheet",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z004_wild_z004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : xsd: un-declared element when content
    is xsd:anyType.
    """
    assert_bindings(
        schema="msData/wildcards/wildZ004.xsd",
        instance="msData/wildcards/wildZ004.xml",
        class_name="RootElem",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z003_wild_z003_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : xsd: test valid instance with elements
    from a different namespace where xsd defint 'any' with ##other
    """
    assert_bindings(
        schema="msData/wildcards/wildZ003_a.xsd",
        instance="msData/wildcards/wildZ003.xml",
        class_name="Elt1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_z002_wild_z002_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : attribute on xsd:any
    processContents="skip"
    """
    assert_bindings(
        schema="msData/wildcards/wildZ002.xsd",
        instance="msData/wildcards/wildZ002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_p006_wild_p006_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=skip
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute not declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP006.xsd",
        instance="msData/wildcards/wildP006.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_p005_wild_p005_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=skip
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP005.xsd",
        instance="msData/wildcards/wildP005.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_p004_wild_p004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=lax
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute not declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP004.xsd",
        instance="msData/wildcards/wildP004.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_p003_wild_p003_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=lax
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP003.xsd",
        instance="msData/wildcards/wildP003.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_p001_wild_p001_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    processContents=strict and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP001.xsd",
        instance="msData/wildcards/wildP001.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o040_wild_o040_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO040.xsd",
        instance="msData/wildcards/wildO040.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o038_wild_o038_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO038.xsd",
        instance="msData/wildcards/wildO038.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o037_wild_o037_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO037.xsd",
        instance="msData/wildcards/wildO037.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o033_wild_o033_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has attributes from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO033.xsd",
        instance="msData/wildcards/wildO033.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o031_wild_o031_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO031.xsd",
        instance="msData/wildcards/wildO031.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o029_wild_o029_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has attributes
    from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO029.xsd",
        instance="msData/wildcards/wildO029.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o027_wild_o027_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO027.xsd",
        instance="msData/wildcards/wildO027.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o026_wild_o026_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has attributes
    from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO026.xsd",
        instance="msData/wildcards/wildO026.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o023_wild_o023_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=http://foobar) with schema targetNamespace=http://foobar and
    instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO023.xsd",
        instance="msData/wildcards/wildO023.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o021_wild_o021_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO021.xsd",
        instance="msData/wildcards/wildO021.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o019_wild_o019_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    with schema targetNamespace=http://foobar and instance document has
    attributes from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO019.xsd",
        instance="msData/wildcards/wildO019.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o018_wild_o018_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    with schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO018.xsd",
        instance="msData/wildcards/wildO018.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o016_wild_o016_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) with
    schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO016.xsd",
        instance="msData/wildcards/wildO016.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o015_wild_o015_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) with
    schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO015.xsd",
        instance="msData/wildcards/wildO015.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o013_wild_o013_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) and instance
    document has attributes from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO013.xsd",
        instance="msData/wildcards/wildO013.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o012_wild_o012_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO012.xsd",
        instance="msData/wildcards/wildO012.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o010_wild_o010_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO010.xsd",
        instance="msData/wildcards/wildO010.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o007_wild_o007_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) and instance document has attributes from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO007.xsd",
        instance="msData/wildcards/wildO007.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o005_wild_o005_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    and instance document has attributes from local Namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO005.xsd",
        instance="msData/wildcards/wildO005.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o004_wild_o004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    and instance document has attributes from other namespaces besides
    target
    """
    assert_bindings(
        schema="msData/wildcards/wildO004.xsd",
        instance="msData/wildcards/wildO004.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o002_wild_o002_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) and
    instance document has attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO002.xsd",
        instance="msData/wildcards/wildO002.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_o001_wild_o001_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) and
    instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO001.xsd",
        instance="msData/wildcards/wildO001.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i012_wild_i012_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    namespaces (##other{1}, A{2}), non-deterministic declaration
    """
    assert_bindings(
        schema="msData/wildcards/wildI012.xsd",
        instance="msData/wildcards/wildI012.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i011_wild_i011_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    namespaces (##other{1}, A{1}), non-deterministic declaration
    """
    assert_bindings(
        schema="msData/wildcards/wildI011.xsd",
        instance="msData/wildcards/wildI011.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i007_wild_i007_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : multiple any in choice with namespaces
    (##other, ##targetNamespace), and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI007.xsd",
        instance="msData/wildcards/wildI007.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i006_wild_i006_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : multiple any in choice with different
    namespaces (a, b, ##targetNamespace, ##local), and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI006.xsd",
        instance="msData/wildcards/wildI006.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i005_wild_i005_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    different namespaces and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI005.xsd",
        instance="msData/wildcards/wildI005.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_i004_wild_i004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : 67191 - ensuring that processContents
    of lax will validate
    """
    assert_bindings(
        schema="msData/wildcards/wildI004.xsd",
        instance="msData/wildcards/wildI004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h012_wild_h012_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and undeclared element,
    processContents=skip)
    """
    assert_bindings(
        schema="msData/wildcards/wildH012.xsd",
        instance="msData/wildcards/wildH012.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h011_wild_h011_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=skip)
    """
    assert_bindings(
        schema="msData/wildcards/wildH011.xsd",
        instance="msData/wildcards/wildH011.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h010_wild_h010_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and undeclared element,
    processContents=lax)
    """
    assert_bindings(
        schema="msData/wildcards/wildH010.xsd",
        instance="msData/wildcards/wildH010.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h009_wild_h009_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=lax)
    """
    assert_bindings(
        schema="msData/wildcards/wildH009.xsd",
        instance="msData/wildcards/wildH009.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h007_wild_h007_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=strict)
    """
    assert_bindings(
        schema="msData/wildcards/wildH007.xsd",
        instance="msData/wildcards/wildH007.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h005_wild_h005_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=skip and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has undeclared elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH005.xsd",
        instance="msData/wildcards/wildH005.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h004_wild_h004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=lax and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has undeclared elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH004.xsd",
        instance="msData/wildcards/wildH004.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_h003_wild_h003_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=lax and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH003.xsd",
        instance="msData/wildcards/wildH003.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g040_wild_g040_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG040.xsd",
        instance="msData/wildcards/wildG040.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g038_wild_g038_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG038.xsd",
        instance="msData/wildcards/wildG038.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g037_wild_g037_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG037.xsd",
        instance="msData/wildcards/wildG037.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g035_wild_g035_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://www.w3.org/1999/xhtml and instance document has
    elements from local
    """
    assert_bindings(
        schema="msData/wildcards/wildG035.xsd",
        instance="msData/wildcards/wildG035.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g033_wild_g033_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG033.xsd",
        instance="msData/wildcards/wildG033.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g031_wild_g031_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=A B C D E ##local
    ##targetNamespace) with schema targetNamespace=http://foobar and
    instance document has elements from all of them
    """
    assert_bindings(
        schema="msData/wildcards/wildG031.xsd",
        instance="msData/wildcards/wildG031.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g027_wild_g027_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG027.xsd",
        instance="msData/wildcards/wildG027.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g026_wild_g026_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG026.xsd",
        instance="msData/wildcards/wildG026.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g023_wild_g023_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG023.xsd",
        instance="msData/wildcards/wildG023.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g021_wild_g021_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG021.xsd",
        instance="msData/wildcards/wildG021.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g018_wild_g018_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG018.xsd",
        instance="msData/wildcards/wildG018.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g016_wild_g016_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG016.xsd",
        instance="msData/wildcards/wildG016.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g015_wild_g015_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG015.xsd",
        instance="msData/wildcards/wildG015.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g013_wild_g013_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG013.xsd",
        instance="msData/wildcards/wildG013.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g012_wild_g012_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG012.xsd",
        instance="msData/wildcards/wildG012.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g010_wild_g010_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has elements from
    both namespaces
    """
    assert_bindings(
        schema="msData/wildcards/wildG010.xsd",
        instance="msData/wildcards/wildG010.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g007_wild_g007_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    and instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG007.xsd",
        instance="msData/wildcards/wildG007.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g006_wild_g006_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) and
    instance document has elements from no namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG006.xsd",
        instance="msData/wildcards/wildG006.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g004_wild_g004_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) and
    instance document has elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG004.xsd",
        instance="msData/wildcards/wildG004.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g002_wild_g002_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) and instance
    document has elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG002.xsd",
        instance="msData/wildcards/wildG002.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild_g001_wild_g001_v(mode, save_output, output_format):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) and instance
    document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG001.xsd",
        instance="msData/wildcards/wildG001.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )
