#!/bin/bash
echo pas | python csci462.py encrypt password-change/original.txt password-change/original3.enc
echo passwo | python csci462.py encrypt password-change/original.txt password-change/original6.enc
echo password1 | python csci462.py encrypt password-change/original.txt password-change/original9.enc
echo password1234 | python csci462.py encrypt password-change/original.txt password-change/original12.enc
echo password1234567 | python csci462.py encrypt password-change/original.txt password-change/original15.enc

echo 1as | python csci462.py encrypt password-change/original.txt password-change/3_1.enc
echo 1asswo | python csci462.py encrypt password-change/original.txt password-change/6_1.enc
echo 1assword1 | python csci462.py encrypt password-change/original.txt password-change/9_1.enc
echo 1assword1234 | python csci462.py encrypt password-change/original.txt password-change/12_1.enc
echo 1assword1234567 | python csci462.py encrypt password-change/original.txt password-change/15_1.enc

echo 12s | python csci462.py encrypt password-change/original.txt password-change/3_2.enc
echo 12sswo | python csci462.py encrypt password-change/original.txt password-change/6_2.enc
echo 12ssword1 | python csci462.py encrypt password-change/original.txt password-change/9_2.enc
echo 12ssword1234 | python csci462.py encrypt password-change/original.txt password-change/12_2.enc
echo 12ssword1234567 | python csci462.py encrypt password-change/original.txt password-change/15_2.enc

echo 123 | python csci462.py encrypt password-change/original.txt password-change/3_3.enc
echo 123swo | python csci462.py encrypt password-change/original.txt password-change/6_3.enc
echo 123sword1 | python csci462.py encrypt password-change/original.txt password-change/9_3.enc
echo 123sword1234 | python csci462.py encrypt password-change/original.txt password-change/12_3.enc
echo 123sword1234567 | python csci462.py encrypt password-change/original.txt password-change/15_3.enc