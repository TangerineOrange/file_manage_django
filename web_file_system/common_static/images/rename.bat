@echo off
set a=141
setlocal EnableDelayedExpansion
for %%n in (*.jpeg) do (
ren "%%n" "abc-!a!.jpeg"
set /A a+=1
)