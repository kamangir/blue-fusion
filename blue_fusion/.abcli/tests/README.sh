#! /usr/bin/env bash

function test_blue_fusion_README() {
    local options=$1

    abcli_eval ,$options \
        blue_fusion build_README
}



