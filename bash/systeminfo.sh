#!/bin/bash

echo "===== INFORMASI SISTEM ====="
echo "User      : $(whoami)"
echo "Hostname  : $(hostname)"
echo "Kernel    : $(uname -r)"
echo "Arsitektur: $(uname -m)"
echo "Tanggal   : $(date)"
echo "Direktori : $(pwd)"
