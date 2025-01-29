#! /usr/bin/env bash

function blue_fusion_bright_browse() {
    local options=$1
    local what=$(abcli_option "$options" what void)

    abcli_browse $(python3 -m blue_fusion.bright \
        get_url \
        --what $what)
}
