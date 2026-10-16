from output.models.saxon_data.simple.simple002_xsd.simple002 import Chap
from output.models.saxon_data.simple.simple002_xsd.simple002 import Doc


obj = Doc(
    chap_or_appx=[
        Doc.Chap(
            section=[
                Chap.Section(
                    value='',
                    nr=1.0
                ),
                Chap.Section(
                    value='',
                    nr=2.0
                ),
                Chap.Section(
                    value=''
                ),
                Chap.Section(
                    value=''
                ),
            ]
        ),
        Doc.Appx(
            section=[
                Chap.Section(
                    value='',
                    nr=1.0
                ),
                Chap.Section(
                    value='',
                    nr=2.0
                ),
                Chap.Section(
                    value=''
                ),
                Chap.Section(
                    value=''
                ),
            ]
        ),
    ]
)
