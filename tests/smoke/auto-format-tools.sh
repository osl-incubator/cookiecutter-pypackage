#!/usr/bin/env bash

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. ${SMOKE_DIR}/base.sh "use_black=yes use_blue=no"
. ${SMOKE_DIR}/base.sh "use_black=no use_blue=yes"
