          ORG    0
          B     GLAVNI             

          ORG   0x18                  ; skok na obradu iznimke IRQ
          B     IRQ_P               

          ORG   0x1C                  ; skok na obradu iznimke FIQ
          B     FIQ_P
          

GLAVNI    ; inicijalizacija stogova
          MSR   CPSR, #0b11010010     ; prelazak u način rada IRQ
          MOV   R13,  #0x10000        ; inicijalizacija R13_irq
          MSR   CPSR, #0b11010011     ; prelazak u način rada SVC
          MOV   R13,  #0xF800         ; inicijalizacija R13_svc
          MSR   CPSR, #0b11010001     ; prelazak u način rada FIQ
          MOV   R13,  #0xFC00         ; inicijalizacija R13_fiq

INIT      LDR   R1, DMAC              ; R1 = adresa DMAC
          LDR   R4, RTC               ; R4 = adresa RTC
       
          ; inicijalizacija DMAC
          MOV   R0, #0x500            ; adresiranje izvora
          STR   R0, [R1, #0x10]

          MOV   R0, #0x700            ; adresiranje odredista
          STR   R0, [R1, #0x14]

          MOV   R0, #0xA              ; postavljanje velicine bloka (10)
          STR   R0, [R1, #0x18]
          
          MOV   R0, #0b10101100       ;konfiguracija, IE = 1, WORD = 10
          STR   R0, [R1,#0x1C]

          MRS   R0, CPSR              ; omogucavanje prekid IRQ
          BIC   R0, R0, #0x80 
          MSR   CPSR, R0

          MRS   R0, CPSR              ; omogucavanje prekid FIQ
          BIC   R0, R0, #0x40 
          MSR   CPSR, R0
         
          MOV   R0, #1                ; omogucujemo kanal DMAC-a
          STR   R0, [R1,#0]
      
LOOP      B     LOOP                  

EOP       SWI   123456


IRQ_P     STMFD SP!, {R1,R2, R3,R4}
         
          MOV   R0, #0x00FF0000       ; brisemo stanje spremnosti u DMAC (stavljamo bilo sta)
          STR   R0, [R0, #0x4]          
          
          LDR   R1, ZAKLJ             ; R1 = 80808080                                 
          STR   R1, 0x728             ; na lokaciju 0x728 stavljamo kraj bloka
        
          LDR   R2, BROJAC            ; ucitavamo brojac
          ADD   R2, R2, #1      
          CMP   R2, #5                    
          BEQ   EOF                   ; ako je brojac = 5, end of function
          
          STR   R2, BROJAC            ; ako nije 5, spremamo trenutni brojac

          
          LDR   R3, RTC            
          
          MOV   R0, #1                ; omogucavanje prekida
          STR   R0, [R3, #0x8] 
          MOV   R0, #0                ; cistimo brojilo
          STR   R0, [R3, #0xC] 
          
          LDR   R4, KONST        
          MOV   R0, R4                ; cekamo 3 sekunde
          STR   R0, [R3, #0x4]        
          MOV   R0, #1                ;RTC generira prekide 
          STR   R0, [R3, #0x10]         

EOF       LDMFD SP!, {R1,R2, R3,R4}   ; spremamo kontekts, end of function         
          BEQ   EOP                   ; ako je brojac = 5, end of program
          SUBS  PC, LR, #4 

FIQ_P     STMFD SP!, {R1, R2}
          LDR   R1, RTC
          LDR   R2, DMAC

          ; reinicijalizacija RTC
          MOV   R0, #0                   
          STR   R0, [R1, #0xC]        ;resetiramo brojac
          STR   R0, [R1, #0x8]        ;onemogucujemo prekit na RTC
          STR   R0, [R1, #0x10]       ;resetiramo CR

          ; reinicijalizacija DMA       
          MOV   R0, #0x500            ; izvorisna adresa
          STR   R0, [R2, #0x10]       
          MOV   R0, #0x700            ;odredisna adresa
          STR   R0, [R2, #0x14]         

          MOV   R0, #1                ; omogucujemo kanal za DMAC
          STR   R0, [R2, #0]            

          LDMFD SP!, {R1, R2}
          SUBS  PC, LR, #4
 

DMAC      DW 0x00FF0000               ; adresa DMAC
RTC       DW 0xFFFF0E00               ; adresa RTC
ZAKLJ     DW 0x80808080               ; zakljucni podatak
KONST     DW 3                         
BROJAC    DW 0                          

          ORG 0x500
          DW 0x00112233, 0x44556677, 0x8899AABB, 0xCCDDEEFF, 0x01234567, 0x89ABCDEF,0x0A1B2C3D, 0x4E5F6789, 0x76543210, 0xFEDCBA98

          ORG 0x700
          DW 0, 0, 0, 0, 0, 0, 0, 0,0 ,0 , 0
