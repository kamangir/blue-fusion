#! /usr/bin/env bash

function test_blue_fusion_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_fusion version ${@:2}"
}



