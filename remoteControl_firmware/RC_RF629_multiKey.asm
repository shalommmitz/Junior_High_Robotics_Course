
; PicBasic Pro Compiler 2.46, (c) 1998, 2005 microEngineering Labs, Inc. All Rights Reserved.  
PM_USED			EQU	1

	INCLUDE	"12F629.INC"

RAM_START       		EQU	00020h
RAM_END         		EQU	0005Fh
RAM_BANKS       		EQU	00001h
BANK0_START     		EQU	00020h
BANK0_END       		EQU	0005Fh
EEPROM_START    		EQU	02100h
EEPROM_END      		EQU	0217Fh

R0              		EQU	RAM_START + 000h
R1              		EQU	RAM_START + 002h
R2              		EQU	RAM_START + 004h
R3              		EQU	RAM_START + 006h
R4              		EQU	RAM_START + 008h
R5              		EQU	RAM_START + 00Ah
R6              		EQU	RAM_START + 00Ch
R7              		EQU	RAM_START + 00Eh
R8              		EQU	RAM_START + 010h
T1              		EQU	RAM_START + 012h
FLAGS           		EQU	RAM_START + 014h
GOP             		EQU	RAM_START + 015h
RM1             		EQU	RAM_START + 016h
RM2             		EQU	RAM_START + 017h
RR1             		EQU	RAM_START + 018h
RR2             		EQU	RAM_START + 019h
_bParam          		EQU	RAM_START + 01Ah
_bRet            		EQU	RAM_START + 01Bh
_buttonPressedPinNumber		EQU	RAM_START + 01Ch
_commandParity   		EQU	RAM_START + 01Dh
_i               		EQU	RAM_START + 01Eh
_mask            		EQU	RAM_START + 01Fh
_msg_0           		EQU	RAM_START + 020h
_msg_1           		EQU	RAM_START + 021h
_msg_2           		EQU	RAM_START + 022h
_msg_3           		EQU	RAM_START + 023h
_numBitsOne      		EQU	RAM_START + 024h
_robotIdAsTransmitted		EQU	RAM_START + 025h
_PORTL           		EQU	 GPIO
_PORTH           		EQU	 GPIO
_TRISL           		EQU	 TRISIO
_TRISH           		EQU	 TRISIO
#define _LED_RFTX        	_GPIO_0
#define _GPIO_0          	 GPIO, 000h
#define _GPIO_1          	 GPIO, 001h
#define _GPIO_2          	 GPIO, 002h
#define _GPIO_5          	 GPIO, 005h
#define _GPIO_4          	 GPIO, 004h
#define _OPTION_REG_7    	 OPTION_REG, 007h
#define _TRISIO_1        	 TRISIO, 001h
#define _TRISIO_2        	 TRISIO, 002h
#define _TRISIO_4        	 TRISIO, 004h
#define _TRISIO_5        	 TRISIO, 005h

; Constants.
_ROBOT_ID        		EQU	00001h
_RIGHT_DURATION  		EQU	00078h
_LEFT_DURATION   		EQU	00078h
_T2400           		EQU	00000h
_T1200           		EQU	00001h
_T9600           		EQU	00002h
_T300            		EQU	00003h
_N2400           		EQU	00004h
_N1200           		EQU	00005h
_N9600           		EQU	00006h
_N300            		EQU	00007h
_OT2400          		EQU	00008h
_OT1200          		EQU	00009h
_OT9600          		EQU	0000Ah
_OT300           		EQU	0000Bh
_ON2400          		EQU	0000Ch
_ON1200          		EQU	0000Dh
_ON9600          		EQU	0000Eh
_ON300           		EQU	0000Fh
_MSBPRE          		EQU	00000h
_LSBPRE          		EQU	00001h
_MSBPOST         		EQU	00002h
_LSBPOST         		EQU	00003h
_LSBFIRST        		EQU	00000h
_MSBFIRST        		EQU	00001h
_CLS             		EQU	00000h
_HOME            		EQU	00001h
_BELL            		EQU	00007h
_BKSP            		EQU	00008h
_TAB             		EQU	00009h
_CR              		EQU	0000Dh
_UnitOn          		EQU	00012h
_UnitOff         		EQU	0001Ah
_UnitsOff        		EQU	0001Ch
_LightsOn        		EQU	00014h
_LightsOff       		EQU	00010h
_Dim             		EQU	0001Eh
_Bright          		EQU	00016h
_CMD_MASK        		EQU	00007h
_LED_MASK        		EQU	00008h
_DIR_MASK        		EQU	00030h
_CMD_PARITY_MASK 		EQU	00040h
_FORWARD_VALUE   		EQU	00030h
_BACK_VALUE      		EQU	00000h
_RIGHT_VALUE     		EQU	00010h
_LEFT_VALUE      		EQU	00020h
	INCLUDE	"RC_RF6~1.MAC"
	INCLUDE	"PBPPIC14.LIB"


	LABEL?L	_gg	
	GOSUB?L	_init_hardware
	MOVE?CB	_ROBOT_ID, _bParam
	GOSUB?L	_getParity
	MUL?BCB	_bRet, 080h, _bRet
	OR?CBB	_ROBOT_ID, _bRet, _robotIdAsTransmitted
	MOVE?CB	001h, _i
	LABEL?L	L00001	
	CMPGT?BCL	_i, _ROBOT_ID, L00002
	HIGH?T	_LED_RFTX
	PAUSE?C	00190h
	LOW?T	_LED_RFTX
	PAUSE?C	00190h
	NEXT?BCL	_i, 001h, L00001
	LABEL?L	L00002	
	INPUT?T	_LED_RFTX

	LABEL?L	_mainLoop	
	CMPNE?BCL	_commandParity, 000h, L00003
	MOVE?CB	001h, _commandParity
	GOTO?L	L00004
	LABEL?L	L00003	
	MOVE?CB	000h, _commandParity
	LABEL?L	L00004	
	GOSUB?L	_waitForButton
	MOVE?BB	_bParam, _msg_0
	GOSUB?L	_getParity
	MUL?BCB	_bRet, 080h, _bRet
	OR?BBB	_msg_0, _bRet, _msg_0
	MOVE?CB	041h, _msg_1
	MOVE?CB	041h, _msg_2
	MOVE?BB	_robotIdAsTransmitted, _msg_3
	XOR?BBB	_msg_3, _msg_0, _msg_3
	XOR?BBB	_msg_3, _msg_1, _msg_3
	XOR?BBB	_msg_3, _msg_2, _msg_3
	MOVE?CB	001h, _i
	LABEL?L	L00005	
	CMPGT?BCL	_i, 004h, L00006
	SERPIN?T	_GPIO_0
	SERMODE?C	_T1200
	SEROUT?C	0AAh
	SEROUT?C	0AAh
	SEROUT?C	0AAh
	SEROUT?C	0AAh
	SEROUT?B	_robotIdAsTransmitted
	SEROUT?B	_msg_0
	SEROUT?B	_msg_1
	SEROUT?B	_msg_2
	SEROUT?B	_msg_3
	MUL?BCW	_i, 00Ah, T1
	PAUSE?W	T1
	NEXT?BCL	_i, 001h, L00005
	LABEL?L	L00006	
	INPUT?T	_LED_RFTX
	PAUSE?C	0C8h
	GOTO?L	_mainLoop

	LABEL?L	_waitForButton	
	MOVE?CB	000h, _bParam
	CMPNE?TCL	_GPIO_1, 000h, L00007
	OR?BCB	_bParam, 001h, _bParam
	LABEL?L	L00007	
	CMPNE?TCL	_GPIO_2, 000h, L00009
	OR?BCB	_bParam, 002h, _bParam
	LABEL?L	L00009	
	CMPNE?TCL	_GPIO_5, 000h, L00011
	OR?BCB	_bParam, 004h, _bParam
	LABEL?L	L00011	
	CMPNE?TCL	_GPIO_4, 000h, L00013
	OR?BCB	_bParam, 008h, _bParam
	LABEL?L	L00013	
	CMPLE?BCL	_bParam, 000h, L00015
	RETURN?	
	LABEL?L	L00015	
	GOTO?L	_waitForButton

	LABEL?L	_getParity	
	MOVE?CB	000h, _numBitsOne
	MOVE?CB	001h, _mask
	MOVE?CB	001h, _i
	LABEL?L	L00017	
	CMPGT?BCL	_i, 008h, L00018
	AND?BBW	_mask, _bParam, T1
	CMPLE?WCL	T1, 000h, L00019
	ADD?BCB	_numBitsOne, 001h, _numBitsOne
	LABEL?L	L00019	
	MUL?BCB	_mask, 002h, _mask
	NEXT?BCL	_i, 001h, L00017
	LABEL?L	L00018	
	MOD?BCB	_numBitsOne, 002h, _bRet
	RETURN?	

	LABEL?L	_init_hardware	
	DISABLE?	
	MOVE?CB	007h, CMCON
	MOVE?CT	000h, _OPTION_REG_7
	MOVE?CT	001h, _TRISIO_1
	MOVE?CT	001h, _TRISIO_2
	MOVE?CT	001h, _TRISIO_4
	MOVE?CT	001h, _TRISIO_5
	MOVE?CB	0FEh, WPU

	ASM?
                
      bsf STATUS, RP0 ;Bank 1
      call 3FFh ;Get the cal value
      movwf OSCCAL ;Calibrate
      bcf STATUS, RP0 ;Bank 0
    

	ENDASM?

	RETURN?	

	END
