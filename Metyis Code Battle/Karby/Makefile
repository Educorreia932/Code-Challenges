##############################################################################
#
#    file                 : Makefile
#    created              : Wed Apr 6 03:53:44 PM WEST 2022
#    copyright            : (C) 2002 TriceraTOP
#
##############################################################################

ROBOT       = Karby
MODULE      = ${ROBOT}.so
MODULEDIR   = drivers/${ROBOT}
SOURCES     = ${ROBOT}.cpp

SHIPDIR     = drivers/${ROBOT}
SHIP        = ${ROBOT}.xml car1-ow1.rgb logo.rgb
SHIPSUBDIRS = 

PKGSUBDIRS  = ${SHIPSUBDIRS}
src-robots-Karby_PKGFILES = $(shell find * -maxdepth 0 -type f -print)
src-robots-Karby_PKGDIR   = ${PACKAGE}-${VERSION}/$(subst ${TORCS_BASE},,$(shell pwd))

include ${MAKE_DEFAULT}

uninstall:
	rm -rf ${libdir}/${MODULEDIR}
	rm -rf ${datadir}/${MODULEDIR}
