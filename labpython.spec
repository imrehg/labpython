[Package Name]
Name=oglib_labpython
Version=1.2
Release=1

[Description]
Description="The LabPython package contains several routines for interfacing to Python."
Summary="OpenG LabPython Tools"
License=LGPL
Copyright="2002 - 2007 Okko Willeboordse, Jim Kring, Rolf Kalbermatter"
Distribution="OpenG Toolkit"
Icon=labpython.bmp
Vendor=OpenG.org
URL=http://openg.org/labpython
Packager="Jim Kring <jim@jimkring.com>"

[Script VIs]

[Dependencies]
Requires="ogrsc_dynamicpalette >= 2.0"
AutoReqProv=FALSE

[Platform]
Exclusive_LabVIEW_Version= >=6.0
Exclusive_LabVIEW_System=All
Exclusive_OS=All

[Files]
Num File Groups=7

[File Group 0]
Source Dir=built/labpython
Target Dir=<user.lib>/_OpenG.lib/labpython
Replace Mode=Always

Num Files=39

File 0=readme.txt
File 1=labpython.llb/PYTHON Close Session__ogtk.vi
File 2=labpython.llb/PYTHON Compile Script__ogtk.vi
File 3=labpython.llb/PYTHON Execute Script__ogtk.vi
File 4=labpython.llb/PYTHON Get Boolean Data__ogtk.vi
File 5=labpython.llb/PYTHON Get Complex Data__ogtk.vi
File 6=labpython.llb/PYTHON Get Complex Matrix__ogtk.vi
File 7=labpython.llb/PYTHON Get Complex Vector__ogtk.vi
File 8=labpython.llb/PYTHON Get Data__ogtk.vi
File 9=labpython.llb/PYTHON Get Float Data__ogtk.vi
File 10=labpython.llb/PYTHON Get Float Matrix__ogtk.vi
File 11=labpython.llb/PYTHON Get Float Vector__ogtk.vi
File 12=labpython.llb/PYTHON Get Integer Data__ogtk.vi
File 13=labpython.llb/PYTHON Get Integer Matrix__ogtk.vi
File 14=labpython.llb/PYTHON Get Integer Vector__ogtk.vi
File 15=labpython.llb/PYTHON Get String Data__ogtk.vi
File 16=labpython.llb/PYTHON Get String Vector__ogtk.vi
File 17=labpython.llb/PYTHON Get Variables__ogtk.vi
File 18=labpython.llb/PYTHON Get Version and Types__ogtk.vi
File 19=labpython.llb/PYTHON New Session__ogtk.vi
File 20=labpython.llb/PYTHON Script Node__ogtk.vi
File 21=labpython.llb/Python Session Refnum__ogtk.ctl
File 22=labpython.llb/PYTHON Set Boolean Data__ogtk.vi
File 23=labpython.llb/PYTHON Set Complex Data__ogtk.vi
File 24=labpython.llb/PYTHON Set Complex Matrix__ogtk.vi
File 25=labpython.llb/PYTHON Set Complex Vector__ogtk.vi
File 26=labpython.llb/PYTHON Set Data__ogtk.vi
File 27=labpython.llb/PYTHON Set Float Data__ogtk.vi
File 28=labpython.llb/PYTHON Set Float Matrix__ogtk.vi
File 29=labpython.llb/PYTHON Set Float Vector__ogtk.vi
File 30=labpython.llb/PYTHON Set Integer Data__ogtk.vi
File 31=labpython.llb/PYTHON Set Integer Matrix__ogtk.vi
File 32=labpython.llb/PYTHON Set Integer Vector__ogtk.vi
File 33=labpython.llb/PYTHON Set Script Text__ogtk.vi
File 34=labpython.llb/PYTHON Set Server Path__ogtk.vi
File 35=labpython.llb/PYTHON Set String Data__ogtk.vi
File 36=labpython.llb/PYTHON Set String Vector__ogtk.vi
File 37=labpython.llb/PYTHON UTIL Format Error Code__ogtk.vi
File 38=labpython.llb/PYTHON VI Tree__ogtk.vi

[File Group 1]
Source Dir=built/labpython
Target Dir=<user.lib>/_OpenG.lib/labpython
Exclusive_OS=Windows NT, Windows 9x
Replace Mode=If Newer
Num Files=1
File 0=lvpython.dll

[File Group 2]
Source Dir=built/labpython
Target Dir=<user.lib>/_OpenG.lib/labpython
Exclusive_OS=Linux
Replace Mode=If Newer
Num Files=1
File 0=lvpython.so

[File Group 3]
Source Dir=built/labpython
Target Dir=<resource>/script
Exclusive_OS=Windows NT, Windows 9x
Replace Mode=If Newer
Num Files=1
File 0=pytscript.dll

[File Group 4]
Source Dir=built/labpython
Target Dir=<resource>/script
Exclusive_OS=Linux
Replace Mode=If Newer
Num Files=1
File 0=pytscript.so

[File Group 5]
Source Dir="Dynamic Palette MNUs"
Target Dir="<user.lib>/_dynamicpalette_dirs/comm"
Replace Mode=Always
Num Files=1
File 0=oglib_labpython.mnu

[File Group 6]
Source Dir="Dynamic Palette MNUs"
Target Dir="<user.lib>/_dynamicpalette_dirs/OpenG"
Replace Mode=Always
Num Files=1
File 0=oglib_labpython.mnu