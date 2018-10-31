

import sys

from pyscreenshot.plugins import wxscreen, gtkpixbuf, qtgrabwindow, qt5grabwindow, \
    scrot, imagemagick, mac_quartz, mac_screencapture, pil, pyside_grabwindow, gnome_screenshot


if sys.platform == 'linux2':
    BACKENDS = [
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
#         pyside_grabwindow.PySideGrabWindow,
        gnome_screenshot.GnomeScreenshotWrapper,
    ]
elif sys.platform == 'darwin':
    BACKENDS = [
        mac_quartz.MacQuartzWrapper,
        mac_screencapture.ScreencaptureWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
#         pyside_grabwindow.PySideGrabWindow,
    ]
elif sys.platform == 'win32':
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
#         pyside_grabwindow.PySideGrabWindow,
    ]
else:
    BACKENDS = [
        pil.PilWrapper,
        wxscreen.WxScreen,
        gtkpixbuf.GtkPixbufWrapper,
        qtgrabwindow.QtGrabWindow,
        qt5grabwindow.Qt5GrabWindow,
        scrot.ScrotWrapper,
        imagemagick.ImagemagickWrapper,
        mac_screencapture.ScreencaptureWrapper,
        mac_quartz.MacQuartzWrapper,
#         pyside_grabwindow.PySideGrabWindow,
        gnome_screenshot.GnomeScreenshotWrapper,
    ]


default_preference = [x.name for x in BACKENDS]
