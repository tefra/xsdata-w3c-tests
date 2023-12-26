from output.models.saxon_data.override.over015_xsd import Doc
from output.models.saxon_data.override.over015_xsd import NotaFooBar
from output.models.saxon_data.override.over015_xsd import StructuredDate


obj = Doc(
    para_or_bezzle=[
        StructuredDate(
            year='2010',
            month='05',
            day='11',
            nota=NotaFooBar.FOO
        ),
        StructuredDate(
            year='2011',
            month='05',
            day='11',
            nota=NotaFooBar.BEZ
        ),
    ]
)
