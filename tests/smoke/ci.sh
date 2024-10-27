#!/usr/bin/env bash
set -e

SMOKE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CHECK_SCHEMA_CMD="python ${SMOKE_DIR}/../scripts/check_schema.py"

# Run the complete smoke tests
. ${SMOKE_DIR}/base.sh "use_circleci=yes use_conda=yes"
. ${SMOKE_DIR}/base.sh "use_circleci=yes use_pyenv=yes"
. ${SMOKE_DIR}/base.sh "use_azure_pipelines=yes use_conda=yes"
. ${SMOKE_DIR}/base.sh "use_azure_pipelines=yes use_pyenv=yes"
. ${SMOKE_DIR}/base.sh "use_gitlab_ci=yes use_conda=yes"
. ${SMOKE_DIR}/base.sh "use_gitlab_ci=yes use_pyenv=yes"

# Check the CI files from template
. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_conda=yes"
pushd /tmp/osl/osl-python-package
  circleci config validate
popd

. ${SMOKE_DIR}/base-template.sh "use_circleci=yes use_pyenv=yes"
pushd /tmp/osl/osl-python-package
  circleci config validate
popd

. ${SMOKE_DIR}/base-template.sh "use_azure_pipelines=yes use_conda=yes"
pushd /tmp/osl/osl-python-package
  ${CHECK_SCHEMA_CMD} ${SMOKE_DIR}/schemas/azure-pipelines.json azure-pipelines.yml
popd

. ${SMOKE_DIR}/base-template.sh "use_azure_pipelines=yes use_pyenv=yes"
pushd /tmp/osl/osl-python-package
  ${CHECK_SCHEMA_CMD} ${SMOKE_DIR}/schemas/azure-pipelines.json azure-pipelines.yml
popd

. ${SMOKE_DIR}/base-template.sh "use_gitlab_ci=yes use_conda=yes"
pushd /tmp/osl/osl-python-package
  ${CHECK_SCHEMA_CMD} ${SMOKE_DIR}/schemas/gitlab-ci.json .gitlab-ci.yml
popd

. ${SMOKE_DIR}/base-template.sh "use_gitlab_ci=yes use_pyenv=yes"
pushd /tmp/osl/osl-python-package
  ${CHECK_SCHEMA_CMD} ${SMOKE_DIR}/schemas/gitlab-ci.json .gitlab-ci.yml
popd
