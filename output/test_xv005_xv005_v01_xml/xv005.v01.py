from output.models.saxon_data.xml_versions.xv005_xsd.xv005 import Doc


obj = Doc(
    item=[
        ':',
        'A',
        '_',
        'a',
        'À',
        'Ø',
        'ø',
        'Ͱ',
        'ͽ',
        '\u1fff',
        '\u200c',
        '⁰',
        'Ⰰ',
        '、',
        '豈',
        'ﷰ',
        '�',
        '𐀀',
        '𠀀',
        '𰀀',
        '\U00040000',
        '\U000e0000',
        '\U000effff',
    ]
)
