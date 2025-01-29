#! /usr/bin/env bash

function blue_fusion() {
    local task=$(abcli_unpack_keyword $1 version)

    abcli_generic_task \
        plugin=blue_fusion,task=$task \
        "${@:2}"
}

abcli_log $(blue_fusion version --show_icon 1)
