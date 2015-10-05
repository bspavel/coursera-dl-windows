# Coursera Downloader for Windows

A windows utility developed with [Coursera Downloader](https://github.com/coursera-dl/coursera-dl) Python Scripts.

# Download
You can get the latest release from here.
 https://github.com/nishad/coursera-dl-windows/releases/latest  
 Download `coursera-dl-win-X.X.X.zip` 

# Usage
```
usage: coursera-dl.exe [-h] [-u USERNAME] [-p PASSWORD] [--on-demand] [-b]                       [--path PATH] [-sl SUBTITLE_LANGUAGE] [--about]                       [-f FILE_FORMATS] [--ignore-formats IGNORE_FORMATS]                       [-sf SECTION_FILTER] [-lf LECTURE_FILTER]                       [-rf RESOURCE_FILTER]                       [--video-resolution VIDEO_RESOLUTION] [--wget [WGET]]                       [--curl [CURL]] [--aria2 [ARIA2]] [--axel [AXEL]]                       [--resume] [-o] [--verbose-dirs] [--quiet] [-r]                       [--combined-section-lectures-nums]                       [--unrestricted-filenames] [-v] [-c COOKIES_FILE]                       [-n [NETRC]] [-k] [--clear-cache] [--hook HOOKS] [-pl]                       [--skip-download] [--debug] [-l LOCAL_PAGE]                       class_names [class_names ...]Download Coursera.org lecture material and resources.optional arguments:  -h, --help            show this help message and exit  --resume              resume incomplete downloads (default: False)  -o, --overwrite       whether existing files should be overwritten (default:                        False)  --verbose-dirs        include class name in section directory name  --quiet               omit as many messages as possible (only printing                        errors)  -r, --reverse         download sections in reverse order  --combined-section-lectures-nums                        include lecture and section name in final files  --unrestricted-filenames                        Do not limit filenames to be ASCII-only  -v, --version         Display the version of udemy-dl and exitBasic options:  class_names           name(s) of the class(es) (e.g. "ml-005")  -u USERNAME, --username USERNAME                        coursera username  -p PASSWORD, --password PASSWORD                        coursera password  --on-demand           [DEPRECATED] get on-demand videos. Do not use this                        option, it is deprecated. The script will try to                        detect course type automatically.  -b, --preview         get videos from preview pages. (Default: False)  --path PATH           path to where to save the file. (Default: current                        directory)  -sl SUBTITLE_LANGUAGE, --subtitle-language SUBTITLE_LANGUAGE                        Choose language to download subtitles. (Default: en)Selection of material to download:  --about               download "about" metadata. (Default: False)  -f FILE_FORMATS, --formats FILE_FORMATS                        file format extensions to be downloaded in quotes                        space separated, e.g. "mp4 pdf" (default: special                        value "all")  --ignore-formats IGNORE_FORMATS                        file format extensions of resources to ignore                        (default: None)  -sf SECTION_FILTER, --section_filter SECTION_FILTER                        only download sections which contain this regex                        (default: disabled)  -lf LECTURE_FILTER, --lecture_filter LECTURE_FILTER                        only download lectures which contain this regex                        (default: disabled)  -rf RESOURCE_FILTER, --resource_filter RESOURCE_FILTER                        only download resources which match this regex                        (default: disabled)  --video-resolution VIDEO_RESOLUTION                        video resolution to download (default: 540p); only                        valid for on-demand courses; only values allowed:                        360p, 540p, 720pExternal downloaders:  --wget [WGET]         use wget for downloading,optionally specify wget bin  --curl [CURL]         use curl for downloading, optionally specify curl bin  --aria2 [ARIA2]       use aria2 for downloading, optionally specify aria2                        bin  --axel [AXEL]         use axel for downloading, optionally specify axel binAdvanced authentication options:  -c COOKIES_FILE, --cookies_file COOKIES_FILE                        full path to the cookies.txt file  -n [NETRC], --netrc [NETRC]                        use netrc for reading passwords, uses default location                        if no path specified  -k, --keyring         use keyring provided by operating system to save and                        load credentials  --clear-cache         clear cached cookiesAdvanced miscellaneous options:  --hook HOOKS          hooks to run when finished  -pl, --playlist       generate M3U playlists for course weeksDebugging options:  --skip-download       for debugging: skip actual downloading of files  --debug               print lots of debug information  -l LOCAL_PAGE, --process_local_page LOCAL_PAGE                        uses or creates local cached version of syllabus page```

# Introduction

[Coursera][1] is arguably the leader in *massive open online courses* (MOOC)
with a selection of more than 300 classes from 62 different institutions [as of
February 2013][13]. Generous contributions by educators and institutions are
making excellent education available to many who could not afford it otherwise.
There are even non-profits with "feet on the ground" in remote areas of the
world who are helping spread the wealth.

This utility makes it easier to batch download lecture resources (e.g., videos, ppt,
etc) for Coursera classes.  Given one or more class names and account credentials,
it obtains week and class names from the *lectures* page, and then downloads
the related materials into appropriately named files and directories.

Why is this helpful?  A utility like [wget][2] can work, but has the
following limitations:

1. Video names have numbers in them, but this does not correspond to
    the actual order.  Manually renaming them is a pain that is best left
    for computers.
2. Using names from the syllabus page provides more informative names.
3. Using `wget` in a for loop picks up extra videos which are not
    posted/linked, and these are sometimes duplicates.

Browser extensions like *DownloadThemAll* is another possibility, but
`coursera-dl` provides more features such as appropriately named files.

This work was originally inspired in part by [youtube-dl][3] by which
I've downloaded many other good videos such as those from Khan Academy.

# Features

  * Support for both regular (i.e., time-based) courses as well as on-demand
    courses.
  * Intentionally detailed names, so that it will display and sort properly
    on most interfaces (e.g., [VLC][4] or MX Video on Android devices).
  * Regex-based section (week) and lecture name filters to download only
    certain resources.
  * File format extension filter to grab resource types you want.
  * Login credentials accepted on command-line or from `.netrc` file.
  * Core functionality tested on major new Windows editions.

# Disclaimer

`coursera-dl` is meant to be used only for your material that Coursera gives
you access to download.

We do not encourage any use that violates their [Terms Of Use][20]. A
relevant excerpt:

> "[...] Coursera grants you a personal, non-exclusive, non-transferable
> license to access and use the Sites. You may download material from the
> Sites only for your own personal, non-commercial use. You may not
> otherwise copy, reproduce, retransmit, distribute, publish, commercially
> exploit or otherwise transfer any material, nor may you modify or create
> derivatives works of the material."

*Note:* You must already have (manually) agreed to the Honor of Code of the
particular courses that you want to use with `coursera-dl`.

## Create an account with Coursera

If you don't already have one, create a [Coursera][1] account and enroll in
a class. See https://www.coursera.org/courses for the list of classes.

## Running the script

Run the exe to download the materials by providing your Coursera account
credentials (e.g. email address and password or a `~/.netrc` file), the
class names, as well as any additional parameters:

    General:                     coursera-dl -u <user> -p <pass> modelthinking-004
    On-Demand course:            coursera-dl -u <user> -p <pass> --on-demand calculus1
    Multiple classes:            coursera-dl -u <user> -p <pass> saas historyofrock1-001 algo-2012-002
    Filter by section name:      coursera-dl -u <user> -p <pass> -sf "Chapter_Four" crypto-004
    Filter by lecture name:      coursera-dl -u <user> -p <pass> -lf "3.1_" ml-2012-002
    Download only ppt files:     coursera-dl -u <user> -p <pass> -f "ppt" qcomp-2012-001
    Use a ~/.netrc file:         coursera-dl -n -- matrix-001
    Get the preview classes:     coursera-dl -n -b ni-001
    Specify download path:       coursera-dl -n --path=C:\Coursera\Classes\ comnetworks-002
    Display help:                coursera-dl --help

**Note:** Some of the options like `-sf` and `-f` may not work with on-demand courses.
Downloading on-demand courses are mutually exclusive with regular courses.

    Maintain a list of classes in a dir:
      Initialize:              mkdir -p CURRENT/{class1,class2,..classN}
      Update:                  coursera-dl -n --path CURRENT `\ls CURRENT`

Note that we *do* support the new On Demand classes. You have to use the
option `--on-demand` for that purpose. You also have to download those
classes *separately* for regular, time-based classes.

Use of a `~/.netrc` file is a good alternative to
specifying both your username (i.e., your email address) and password every
time on the command line. To use it, simply add a line like the one below to
a file named `.netrc` in your home directory (or the [equivalent][8], if you
are using Windows) with contents like:

    machine coursera-dl login <user> password <pass>

Create the file if it doesn't exist yet.  From then on, you can switch from
using `-u` and `-p` to simply call `coursera-dl` with the option `-n`
instead.  This is especially convenient, as typing usernames (email
addresses) and passwords directly on the command line can get tiresome (even
more if you happened to choose a "strong" password).

## Resuming downloads

In default mode when you interrupt the download process by pressing
<kbd>CTRL</kbd>+<kbd>C</kbd>, partially downloaded files will be deleted from your disk and
you have to start the download process from the begining. If your
download was interrupted by something other than KeyboardInterrupt
(<kbd>CTRL</kbd>+<kbd>C</kbd>) like sudden system crash, partially downloaded files will
remain on your disk and the next time you start the process again,
these files will be discraded from download list!, therefore it's your
job to delete them manually before next start. For this reason we
added an option called `--resume` which continues your downloads from
where they stopped:

	coursera-dl -u <user> -p <pass> --resume sdn1-001

This option can also be used with external downloaders:

	coursera-dl --wget -u <user> -p <pass> --resume sdn1-001

*Note 1*: Some external downloaders use their own built-in resume feature
which may not be compatible with others, so use them at your own risk.

*Note 2*: Remember that in resume mode, interrupted files **WON'T** be deleted from
your disk.

**NOTE**: If your password contains punctuation, quotes or other "funny
characters" (e.g., `<`, `>`, `#`, `&`, `|` and so on), then you may have to
escape them. One of the better ways to do so is to
enclose your password in single quotes, so that you don't run into
problems.  See [issue #213][issue213] for more information.

# Troubleshooting

If you have problems when downloading class materials, please try to see if
one of the following actions solve your problem:

* Make sure the class name you are using corresponds to the resource name
  used in the URL for that class:
    `https://class.coursera.org/<CLASS_NAME>/class/index`

* To download an On Demand course, use the `--on-demand` option of the
  program.

* Have you tried to clean the cached cookies/credentials with the
  `--clear-cache` option?

* Note that many courses (most, perhaps?) may remove the materials after a
  little while after the course is completed, while other courses may retain
  the materials up to a next session/offering of the same course (to avoid
  problems with academic dishonesty, apparently).
  <br><br>
  In short, it is not guaranteed that you will be able to download after the
  course is finished and this is, unfortunately, nothing that we can help
  you with.

* One can export a Netscape-style cookies file with a browser extension ([1][9], [2][10])
  and use it with the `-c` option. This comes in handy
  when the authentication via password is not working (the authentication
  process changes now and then).

* If results show 0 sections, you most likely have provided invalid
  credentials (username and/or password in the command line or in your
  `.netrc` file).

* For courses that have not started yet, but have had a previous iteration
  sometimes a preview is available, containing all the classes from the last
  course. These files can be downloaded by passing the `--preview`
  parameter.

* If you get an error like `Could not find class: <CLASS_NAME>`, then:
    * Verify that the name of the course is correct. Current class
    names in coursera are composed by a short course name e.g. `class` and
    the current version of the course (a number). For example, for a
    class named `class`, you would have to use `class-001`, `class-002`
    etc.
    * Second, verify that you are enrolled in the course. You won't be
    able to access the course materials if you are not officially
    enrolled and agreed to the honor course *via the website*.

* If:
    * You get an error when using `-n` to specify that you want to use a
      `.netrc` file and,
    * You want the script to use your default netrc file and,
    * You get a message saying `coursera-dl: error: too few arguments`  
    
      Then you should specify `--` as an argument after `-n`, that is, `-n --`
      or change the order in which you pass the arguments to the script, so that
      the argument after `-n` begins with an hyphen (`-`).  Otherwise, Python's
      `argparse` module will think that what you are passing is the name of the
      netrc file that you want to use. See issue #162.

# Filing an issue/Reporting a bug

When reporting bugs against `coursera-dl`, please don't forget to include
enough information so that you can help us help you:

* Is the problem happening with the latest version of the exe?
* What operating system are you using?
* Which version of the script you are using? (Output of `coursera-dl.exe -v`)
* What is the course that you are trying to access?
* What is the precise command line that you are using (feel free to hide
  your username and password with asterisks, but leave all other
  information untouched).
* What are the precise messages that you get? Please, use the `--debug`
  option before posting the messages as a bug report. Please, copy and paste
  them.  Don't reword/paraphrase the messages.

# Contact

Please, post bugs and issues on [github][11]. 

[1]: https://www.coursera.org
[2]: http://sourceforge.net/projects/gnuwin32/files/wget/1.11.4-1/wget-1.11.4-1-setup.exe
[3]: https://rg3.github.com/youtube-dl
[4]: https://f-droid.org/repository/browse/?fdid=org.videolan.vlc
[5]: http://www.crummy.com/software/BeautifulSoup
[6]: http://pypi.python.org/pypi/argparse
[7]: http://pypi.python.org/pypi/setuptools
[8]: http://stackoverflow.com/a/6031266/962311
[9]: https://chrome.google.com/webstore/detail/lopabhfecdfhgogdbojmaicoicjekelh
[10]: https://addons.mozilla.org/en-US/firefox/addon/export-cookies
[11]: https://github.com/nishad/coursera-dl-windows/issues
[12]: https://twitter.com/jplehmann
[13]: http://techcrunch.com/2013/02/20/coursera-adds-29-schools-90-courses-and-4-new-languages-to-its-online-learning-platform
[14]: http://www.tunapanda.org
[15]: https://github.com/html5lib/html5lib-python
[16]: http://docs.python-requests.org/en/latest/
[17]: http://www.pip-installer.org/en/latest/
[18]: http://python-distribute.org/pip_distribute.png
[19]: https://pypi.python.org/pypi/six/
[20]: https://www.coursera.org/about/terms
[21]: https://twitter.com/rtdbrito
[22]: http://pypi.python.org/
[23]: http://pypi.python.org/pypi/coursera
[issue213]: https://github.com/coursera-dl/coursera-dl/issues/213
