#/bin/sh
SCRIPTPATH=$( cd $(dirname $0) ; pwd -P  )
git config --global core.excludesfile $SCRIPTPATH/global_ignore
