#! /usr/bin/env bash

function blue_fusion_bright_install() {
    local options=$1
    local recreate_env=$(abcli_option_int "$options" recreate_env 0)

    if [[ -d "$abcli_path_git/BRIGHT" ]]; then
        abcli_log "✅  BRIGHT"
    else
        abcli_git_clone https://github.com/ChenHongruixuan/BRIGHT
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$abcli_is_github_workflow" == true ]] ||
        [[ "$abcli_is_sagemaker_system" == true ]] &&
        return 0

    if [[ "$recreate_env" == 1 ]]; then
        abcli_conda_rm name=bright-benchmark
        [[ $? -ne 0 ]] && return 1
    fi

    local exists=$(abcli_conda_exists name=bright-benchmark)
    if [[ "$exists" == 0 ]]; then
        # https://github.com/ChenHongruixuan/BRIGHT
        conda create -n bright-benchmark pip --yes
        [[ $? -ne 0 ]] && return 1

        conda activate bright-benchmark
        [[ $? -ne 0 ]] && return 1

        pip install -r \
            $abcli_path_git/blue-fusion/requirements.txt
        [[ $? -ne 0 ]] && return 1

        pushd $abcli_path_git/blue-fusion >/dev/null
        pip3 install -e .
        [[ $? -ne 0 ]] && return 1
        popd >/dev/null
    fi
}

function abcli_install_blue_fusion_bright() {
    blue_fusion_bright_install "$@"
}

abcli_install_module blue_fusion_bright 1.3.1
