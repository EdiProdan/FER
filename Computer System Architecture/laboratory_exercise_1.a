        ORG 0                   ;krecemo program od 0
        MOV R0, #0x500          ;u R0 stavljamo adresu 500 (pocetni blok)
        MOV R5, #0x1000         ;u R5 stavljamo adresu 1000 (rezultantni blok)
        MOV SP, #0x5000         ;stog postavljamo na adresu 5000
       
PETLJA  LDR R1, [R0], #4        ;R1 = operacija
        LDR R2, [R0], #4        ;R2 = opA
        LDR R3, [R0], #4        ;R3 = opB
        LDR R6, ZAKLJ_A         ;R6 = 80808080
        CMP R1, R6              ;provjeravamo operaciju s maskom zavrsetka bloka, 0, 1, 2, 3
        BEQ KRAJ
        CMP R1, #0
        BEQ FADD
        CMP R1, #1
        BEQ FSUB
        CMP R1, #2
        BEQ FMUL
        CMP R1, #3
        BEQ FDIV
        
        
        
FADD    ADD R4,R2,R3            ;R4 = R2 + R3
        STR R4, [R5], #4        ;spremi R4 na lokaciju 1000 i povisi rezultantni blok
        B   PETLJA

FSUB    SUB R4, R2, R3
        STR R4, [R5], #4 
        B   PETLJA

FMUL    MUL R4, R2, R3
        STR R4, [R5], #4 
        B   PETLJA

FDIV    CMP R2, #0              ;testiramo ako je opA = 0
        STREQ R4, [R5], #0      ;u R4 spremamo 0
        BEQ PETLJA              ;vracamo se na pocetak petlje
        CMP R3, #0
        STREQ R4, [R5], #0
        BEQ PETLJA

        LDR R9, NEG             ;-1
        LDR R7, MASKA           ;100..0

        AND   R8, R7, R2        ;u R8 spremimo mnozenje maske i opA
        CMP   R8, #0x80000000   ;ako se u R8 na najvisem bitu nalazi 1, znaci da je opA neg
        MULEQ R10,R2, R9        ;ako je istina, u R10 spremimo apsolutnu vrijednost opA
        MOVEQ R2, R10           ;R10 premjestimo u R2

        AND   R12, R7, R3       ;analogno za opB
        CMP   R12, #0x80000000
        MULEQ R11,R3,R9
        MOVEQ R3, R11       

                                ;u sljedecim linijama provjeravamo ako su se koristili 
                                ;registri R10 i R11, ako jesu znaci da je taj broj negativan

        MOV R8, #0              ;brojac = 0

        CMP   R10, #0           ;provjeravamo ako je R10 negativan
        ADDNE R8, R8, #1        ;brojac++

        CMP   R11, #0           ;analogno za R11
        ADDNE R8, R8, #1


        STMFD   SP!, {R2,R3}    ;u stog stavljamo opA i opB
        SUB     SP, SP, #4      ;pripremamo mjesta za rezultat

        BL      DIJELI

        LDMFD   SP!,{R4}        ;dohvat rezultata
        LDR R12, ONE            ;broj 1 stavljamo u R12
        MOV R10, R4             ;R10 koristimo kao tmp 
        MUL R11, R10, R12       ;mnozimo rezultat (u R10) s jedan
        CMP R8,  #1             ;provjeravamo ako je brojac 1
                                ;ako je, znaci da je jedan od operanad negativan
        MULEQ R11,R10, R9       ;sve mnozimo s -1
        
        STR R11, [R5], #4       ;spremanje rezultata
        B   PETLJA

;pocetak dijeli
DIJELI  STMFD SP!,{R4, R2, R3}  ;stavljamo argumente
        LDR   R2, [SP, #16]     ;R2 = R2
        LDR   R3, [SP, #20]     ;R3 = R3
        MOV   R4, #0            ;brojac
 
LOOP    CMP R2, R3              ;ako je opA manji od opB, izadi
        BLO VAN
      
        SUB R2, R2, R3          ;opA = opA - opB
        ADD R4, R4, #1          ;brojac++
        
        B   LOOP                ;ponovi dok opA nije manji
       
VAN     STR   R4, [SP, #12]     ; spremi rezultat
        LDMFD SP!, {R4, R2, R3} ; obnovi kontekst 
        MOV   PC, LR
;kraj dijeli
      

KRAJ    MVN R4, #0              ;FFFF FFFF
        STR R4, [R5]            ;spremi ga u kraj rezultantnog bloka
       
        SWI 0x123456            ;kraj programa

ONE     DW 1
NEG     DW 0xFFFFFFFF
MASKA   DW 0x80000000

        ORG 0x500
        DW      0x3, 0xFFFFFEFF, 0x00000010     ; -257 / 16 = -16 0xFFFF FFF0
        DW      0x1, 0x1F4, 0xFFFFFD44          ; 500 - (-700) = 1200 0x0000 04B0
        DW      0x2, 0xFFFFFFFE, 0xA            ; -2 * 10 = -20 0xFFFF FFEC
        DW      0x3, 0xFFFFF000, 0xFFFFFFC0     ; -4096 / -64 = 64 0x0000 0040
        DW      0x80808080
      
ZAKLJ_A DW 0x80808080
        ORG 0x1000
        DW 0, 0, 0, 0, 0
