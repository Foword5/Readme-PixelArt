errorAction = """
Usage : python3 main.py [action]

Possible actions :
    - template [year] : generate the template for the given year
    - commit : commit the template for the given year
    - visualize : visualize the template
"""

generationSuccess = """
The template for the year {} has been successfully generated in the file {}.
You can edit it and set any value from 0 (black) to 4 (bright green).
"""

errorTemplate = """
The template file is not correctly formatted.
"""

errorPixelValue = """
Invalid pixel value at position ({}, {}).
"""

errorVisualize = """
The template file is not correctly formatted. Some white square where placed in the invalids position.
"""

commitSuccess = """
All the commits have been successfully done. Don't forget to push them !
"""