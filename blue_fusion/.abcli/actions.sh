#! /usr/bin/env bash

function blue_fusion_action_git_before_push() {
    blue_fusion build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    blue_fusion pypi build
}



