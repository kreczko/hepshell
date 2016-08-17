#!/bin/bash
drop_from_path()
{
   # Assert that we got enough arguments
   if test $# -ne 2 ; then
      echo "drop_from_path: needs 2 arguments"
      return 1
   fi

   p=$1
   drop=$2

   newpath=`echo $p | sed -e "s;:${drop}:;:;g" \
                          -e "s;:${drop};;g"   \
                          -e "s;${drop}:;;g"   \
                          -e "s;${drop};;g"`
}


if [ -n "${HEP_PROJECT_ROOT}" ] ; then
   old_ntpbase=${HEP_PROJECT_ROOT}
fi


if [ "x${BASH_ARGV[0]}" = "x" ]; then
    if [ ! -f bin/env.sh ]; then
        echo ERROR: must "cd where/NTupleProdcution/is" before calling ". bin/env.sh" for this version of bash!
        HEP_PROJECT_ROOT=; export HEP_PROJECT_ROOT
        return 1
    fi
    HEP_PROJECT_ROOT="$PWD"; export HEP_PROJECT_ROOT
else
    # get param to "."
    envscript=$(dirname ${BASH_ARGV[0]})
    HEP_PROJECT_ROOT=$(cd ${envscript}/..;pwd); export HEP_PROJECT_ROOT
fi

if [ -n "${old_ntpbase}" ] ; then
   if [ -n "${PATH}" ]; then
      drop_from_path "$PATH" ${old_ntpbase}/bin
      PATH=$newpath
   fi
   if [ -n "${PYTHONPATH}" ]; then
      drop_from_path $PYTHONPATH ${old_ntpbase}/python
      PYTHONPATH=$newpath
   fi
fi


if [ -z "${PATH}" ]; then
   PATH=$HEP_PROJECT_ROOT/bin; export PATH
else
   PATH=$HEP_PROJECT_ROOT/bin:$PATH; export PATH
fi

if [ -z "${PYTHONPATH}" ]; then
   PYTHONPATH=$HEP_PROJECT_ROOT/python; export PYTHONPATH
else
   PYTHONPATH=$HEP_PROJECT_ROOT/python:$PYTHONPATH; export PYTHONPATH
fi

# for CMSSW
if [ -f /cvmfs/cms.cern.ch/cmsset_default.sh ]; then
	source /cvmfs/cms.cern.ch/cmsset_default.sh
	export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git
fi

# CRAB submission
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3Releases#Improvements_enhancements_change
if [ -f /cvmfs/cms.cern.ch/crab3/crab.sh ]; then
	source /cvmfs/cms.cern.ch/crab3/crab.sh
fi

# for grid tools
#source /cvmfs/grid.cern.ch/etc/profile.d/setup-cvmfs-ui.sh

# for hadoop, needs to run after grid tools
#if [[ -d "/usr/java/jdk1.7.0_67-cloudera" ]]; then
#	export JAVA_HOME=/usr/java/jdk1.7.0_67-cloudera
#	export PATH=$JAVA_HOME/bin:$PATH
#else
#	# use system default
#	export JAVA_HOME=
#fi

unset old_ntpbase
unset envscript
