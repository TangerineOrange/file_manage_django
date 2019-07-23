@echo off
set a=100
setlocal EnableDelayedExpansion
for %%n in (*.jpg) do (
ren "%%n" "car-!a!.jpg"
set /A a+=1
)