#! /usr/bin/env bash

function test_blue_fusion_help() {
    local options=$1

    local module
    for module in \
        "@fusion" \
        \
        "@fusion pypi" \
        "@fusion pypi browse" \
        "@fusion pypi build" \
        "@fusion pypi install" \
        \
        "@fusion pytest" \
        \
        "@fusion test" \
        "@fusion test list" \
        \
        "@fusion bright" \
        "@fusion bright browse" \
        "@fusion bright install" \
        \
        "@fusion browse" \
        \
        "blue_fusion"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
