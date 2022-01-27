pip3 install auto-py-to-exe
@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin
::
python -m auto_py_to_exe