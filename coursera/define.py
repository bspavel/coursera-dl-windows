# -*- coding: utf-8 -*-

"""
This module defines the global constants.
"""

import os
import getpass
import tempfile

COURSERA_URL = 'https://www.coursera.org'
AUTH_URL = 'https://accounts.coursera.org/api/v1/login'
AUTH_URL_V3 = 'https://www.coursera.org/api/login/v3'
CLASS_URL = 'https://class.coursera.org/{class_name}'
OPENCOURSE_CONTENT_URL = 'https://www.coursera.org/api/opencourse.v1/course/{class_name}'
OPENCOURSE_VIDEO_URL = 'https://www.coursera.org/api/opencourse.v1/video/{video_id}'

ABOUT_URL = ('https://api.coursera.org/api/catalog.v1/courses?'
             'fields=largeIcon,photo,previewLink,shortDescription,smallIcon,'
             'smallIconHover,universityLogo,universityLogoSt,video,videoId,'
             'aboutTheCourse,targetAudience,faq,courseSyllabus,courseFormat,'
             'suggestedReadings,instructor,estimatedClassWorkload,'
             'aboutTheInstructor,recommendedBackground,subtitleLanguagesCsv&'
             'q=search&query={class_name}')

AUTH_REDIRECT_URL = ('https://class.coursera.org/{class_name}'
                     '/auth/auth_redirector?type=login&subtype=normal')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# define a per-user cache folder
if os.name == "posix":  # pragma: no cover
    import pwd
    _USER = pwd.getpwuid(os.getuid())[0]
else:
    _USER = getpass.getuser()

PATH_CACHE = os.path.join(tempfile.gettempdir(), _USER + "_coursera_dl_cache")
PATH_COOKIES = os.path.join(PATH_CACHE, 'cookies')
