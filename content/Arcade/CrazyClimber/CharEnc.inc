;-----------------------------------------------------------------------------
; Character table encoded values
;
; These equates define the character table for screen display for
; Crazy Climber
;-----------------------------------------------------------------------------
DIG0_EN			.equ			$00
DIG1_EN			.equ			$01
DIG2_EN			.equ			$02
DIG3_EN			.equ			$03
DIG4_EN			.equ			$04
DIG5_EN			.equ			$05
DIG6_EN			.equ			$06
DIG7_EN			.equ			$07
DIG8_EN			.equ			$08
DIG9_EN			.equ			$09
A_EN			.equ			$0A
B_EN			.equ			$0B
C_EN			.equ			$0C
D_EN			.equ			$0D
E_EN			.equ			$0E
F_EN			.equ			$0F
G_EN			.equ			$10
H_EN			.equ			$11
I_EN			.equ			$12
J_EN			.equ			$13
K_EN			.equ			$14
L_EN			.equ			$15
M_EN			.equ			$16
N_EN			.equ			$17
O_EN			.equ			$18
P_EN			.equ			$19
Q_EN			.equ			$1A
R_EN			.equ			$1B
S_EN			.equ			$1C
T_EN			.equ			$1D
U_EN			.equ			$1E
V_EN			.equ			$1F
W_EN			.equ			$20
X_EN			.equ			$21
Y_EN			.equ			$22
Z_EN			.equ			$23
EXCLAMATION_EN	.equ			$28				; !
QUOTE_EN		.equ			$28				; '
TIMES_EN		.equ			$2A				; x
MINUS_EN		.equ			$2B				; -
PERIOD_EN		.equ			$2C				; Period
COLON_EN		.equ			$2D				; Colon
PERIODCOMMA_EN	.equ			$2F				; Period & Comma (.,) together
; $30 - $37 is the "Nichibutsu" graphic characters used with the title screen
; $38 - $3B is the high score cursor sprite (Sprite $0E)
RUBL_EN			.equ			$3C				; Left half of Rub (High score registration)
RUBR_EN			.equ			$3D				; Right half of Rub (High score registration)
ENDL_EN			.equ			$3E				; Left half of End (High score registration)
ENDR_EN			.equ			$3F				; Right half of End (High score registration)
SP_EN			.equ			$52				; Space

RBORDER1_EN		.equ			$7C				; Right boarder (leftmost)
RBORDER2_EN		.equ			$7D				; Right boarder (rightmost)
LBORDER_EN		.equ			$7E				; Left screen border

PLAYER_EN		.equ			$7F				; Players remaining (little guy)

SPRITE_HS_CURSOR .equ			$0E				; High score cursor sprite

;-----------------------------------------------------------------------------
; Character colors
;-----------------------------------------------------------------------------
TAN_CHAR_COLOR		.equ		$0A				; Light tan
GREEN_CHAR_COLOR	.equ		$0B				; Green
PURPLE_CHAR_COLOR	.equ		$1E				; Purple
NOCHANGE_CHAR_COLOR	.equ		$FF				; Do not change color plane


