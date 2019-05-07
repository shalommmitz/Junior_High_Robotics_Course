PATH=C:\PBP;%path%
ECHO Compiling.... Please Wait.
C:\PBP\PBP.EXE  -ol -p12F629 RC_RF629.pbp
@del RC_RF629.ASM
@del RC_RF629.MAC
