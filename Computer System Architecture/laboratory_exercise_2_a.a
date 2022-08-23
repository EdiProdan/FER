           ORG   0
           B     GLAVNI
           ORG   0x18

IRQ_P      STMFD SP!, {R0, R1, R2, R3}
        
           LDR   R0, RTC                 ; adresa RTC
           LDR   R2, GPIO                ; adresa GPIO
           LDR   R3, STANJE              ; stanjE
    
IZ_1_U_2   CMP   R3, #0                  ; provjeri ako je stanje 0
           MOVEQ R3, #1                  ; postavi stanje na sljedece
           STREQ R3, STANJE            
           MOVEQ R1, #0b00100000         ; crveno - 5 bit
           STREQ R1, [R2, #0x0]          ; spremi na A vrata
           BEQ   VAN                    


IZ_2_U_3   CMP   R3, #1                  
           MOVEQ R3, #2                  
           STREQ R3, STANJE             
           MOVEQ R1, #0b01100000         ; zuto - 6 bit, zeleno - 7 bit
           STREQ R1, [R2, #0x0]          
           BEQ   VAN                    

IZ_3_U_4   CMP   R3, #2                  
           MOVEQ R1, #0b10000000         ; zeleno - 7 bit
           STREQ R1, [R2, #0x0]          
           MOVEQ R3, #3                  
           STREQ R3, STANJE             
           BEQ   VAN                   

IZ_4_U_1   CMP   R3, #3                  
           MOVEQ R3, #0                  ; povecaj stanje na prvo (0)
           STREQ R3, STANJE              
           MOVEQ R1, #0b01000000         ; zuto = 6 bit
           STREQ R1, [R2, #0x0]        
                                 
VAN        MOV   R1, #0
           STR   R1, [R0, #0x8]          ; ne postavljamo prekide
           STR   R1, [R0, #0xC]          ; resetiramo brojilo

           LDMFD SP!, {R0, R1, R2, R3}
           SUBS  PC, LR, #4
     

GLAVNI     ; stog za irq
           MSR   CPSR, #0b11010010           
           MOV   R13, #0x10000  
           ; stog za svc             
           MSR   CPSR, #0b11010011           
           MOV   R13, #0xF800                
  
           ; inicijalizacija GPIO
           LDR   R2, GPIO                ; GPIO
           MOV   R1, #0b11100000         ; postavljanje pocetnih LED lampica
           STR   R1, [R2, #0x8]          ; spremanje na A port

           ; inicijalizacija RTC
           LDR   R0, RTC                 ; RTC
 
           LDR   R4, KONST               ; ucitavamo konstantu
           MOV   R1,  R4                 
           STR   R1, [R0, #0x4]          

           MOV   R1, #1                  ; omogucujemo prekide
           STR   R1, [R0, #0x10]        
        
           MOV   R1, #0                  ; brisemo LR
           STR   R1, [R0, #0xC]  

           MRS   R5, CPSR                ; dopustamo irq prekide
           BIC   R5, R5, #0b10000000    
           MSR   CPSR, R5               

RADI       B     RADI                    ; radimo posao
       

GPIO       DW 0xFFFF0B00
RTC        DW 0xFFFF0E00

KONST      DW 5                          ; 5s * 1Hz = 5

STANJE     DW 0
