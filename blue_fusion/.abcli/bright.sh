#! /usr/bin/env bash

function blue_fusion_bright() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=blue_fusion_bright_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m blue_fusion.bright "$@"
}

abcli_source_caller_suffix_path /bright
