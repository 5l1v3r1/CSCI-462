#!/bin/bash
echo pas | python csci462.py encrypt plaintext-change/original.txt plaintext-change/original3.enc
echo passwo | python csci462.py encrypt plaintext-change/original.txt plaintext-change/original6.enc
echo password1 | python csci462.py encrypt plaintext-change/original.txt plaintext-change/original9.enc
echo password1234 | python csci462.py encrypt plaintext-change/original.txt plaintext-change/original12.enc
echo password1234567 | python csci462.py encrypt plaintext-change/original.txt plaintext-change/original15.enc

echo pas | python csci462.py encrypt plaintext-change/change5.txt plaintext-change/change5_3.enc
echo passwo | python csci462.py encrypt plaintext-change/change5.txt plaintext-change/change5_6.enc
echo password1 | python csci462.py encrypt plaintext-change/change5.txt plaintext-change/change5_9.enc
echo password1234 | python csci462.py encrypt plaintext-change/change5.txt plaintext-change/change5_12.enc
echo password1234567 | python csci462.py encrypt plaintext-change/change5.txt plaintext-change/change5_15.enc

echo pas | python csci462.py encrypt plaintext-change/change10.txt plaintext-change/change10_3.enc
echo passwo | python csci462.py encrypt plaintext-change/change10.txt plaintext-change/change10_6.enc
echo password1 | python csci462.py encrypt plaintext-change/change10.txt plaintext-change/change10_9.enc
echo password1234 | python csci462.py encrypt plaintext-change/change10.txt plaintext-change/change10_12.enc
echo password1234567 | python csci462.py encrypt plaintext-change/change10.txt plaintext-change/change10_15.enc