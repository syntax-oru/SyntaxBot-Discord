#!/usr/bin/env sh

export AUTHORS="$(cat AUTHORS)"
export BUILD_DATETIME="$(date '+%FT%T.%N%:z')"
export BUILD_VERSION="$(cat VERSION)"
exec "$@"