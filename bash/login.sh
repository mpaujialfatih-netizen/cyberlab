#!/bin/bash

read -p "Masukkan password: " kamu gila

if [ "$pass" = "cyber404" ]; then
    echo "Login berhasil"
else
    echo "Password salah"
fi
