        org 0
glavni 
        lui    sp, %hi(0x10000)            ; inicijalizacija sp
        addi   sp, sp, %lo(0x10000)

        lui    s0, %hi(0xFFFF0F00)         ; inicijalizacija GPIO
        addi   s0, s0, %lo(0xFFFF0F00)
      
        addi   s1, s1, 0x500               ; adresa pocetka bloka
        lw     a0, 0(s1)                   ; na a0(x10) nam se nalazi podatak      
        
        addi   a1,x0,0x0D
        jal    ra, lcdwr
        
        jal    ra, pretvori                ; pozivamo potprogram gdje obavljamo pretvorbu i ispis
 
        addi   a1,x0,0x0A
        jal    ra, lcdwr                   ; uklanjanje parametara sa stoga

        halt                               ; zaustavljamo procesor


pretvori                      
        addi   sp, sp, -12                 ; spremanje konteksta                  
        sw     t0, 0(sp)
        sw     a1, 4(sp)
        sw     ra, 8(sp)
        
startf  ;start function
        addi   t0, x0, 100                 ; postavljamo t0 na 100
        beq    a0, t0, C                   ; ako je a0 == 100 upisujemo C
        
        addi   t0, x0, 90
        bge    a0, t0, XC                  ; a0 >= 90

        addi   t0, x0, 50
        bge    a0, t0, L                   ; a0 >= 50

        addi   t0, x0, 40
        bge    a0, t0, XL                  ; a0 >= 40
        
        addi   t0, x0, 10
        bge    a0, t0, X                   ; a0 >= 10

        addi   t0, x0, 9
        bge    a0, t0, IX                  ; a0 >= 9

        addi   t0, x0, 5
        bge    a0, t0, V                   ; a0 >= 5

        addi   t0, x0, 4
        bge    a0, t0, IV                  ; a0 >= 4

        addi   t0, x0, 1                   ; a0 >= 1
        bge    a0, t0, I
       
        lw     t0, 0(sp)                   ; obnova konteksta
        lw     a1, 4(sp)
        lw     ra, 8(sp)
        addi   sp, sp, 12

        jalr   x0,0(ra)                              


C       addi   a0, a0, -100                ; smanjujemo vrijednost za 100
        addi   a1, x0, 0x43                ; postavljamo registar na ASCII vrijednost C
        jal    ra, lcdwr
        jal    ra, startf                  ; skok u pocetak funkcije (start function)

XC      addi   a0, a0, -90                      
        addi   a1, x0, 0x58                ; ASCII X
        jal    ra, lcdwr
        addi   a1, x0, 0x43                ; ASCII C
        jal    ra, lcdwr
        jal    ra, startf                  

L       addi   a0, a0, -50                     
        addi   a1, x0, 0x4C                ; ASCII L
        jal    ra, lcdwr
        jal    ra, startf                     
        
XL      addi   a0, a0, -40                      
        addi   a1, x0, 0x58                ; ASCII X
        jal    ra, lcdwr
        addi   a1, x0, 0x4C                ; ASCII L
        jal    ra, lcdwr
        jal    ra, startf                      

X       addi   a0, a0, -10                                            
        addi   a1, x0, 0x58                ; ASCII X
        jal    ra, lcdwr
        jal    ra, startf      

IX      addi   a0, a0, -9                      
        addi   a1, x0, 0x49                ; ASCII I
        jal    ra, lcdwr
        addi   a1, x0, 0x58                ; ASCII X
        jal    ra, lcdwr
        jal    ra, startf                      
               
V       addi   a0, a0, -5                                            
        addi   a1, x0, 0x56                ; ASCII V
        jal    ra, lcdwr
        jal    ra, startf      

IV      addi   a0, a0, -4                     
        addi   a1, x0, 0x49                ; ASCII I
        jal    ra, lcdwr
        addi   a1, x0, 0x56                ; ASCII V
        jal    ra, lcdwr
        jal    ra, startf                      

I       addi   a0, a0, -1                  
        addi   a1, x0, 0x49                ; ASCII I
        jal    ra, lcdwr
        jal    ra, startf                      
      
lcdwr
        andi   a1,a1,0x7F
        sb     a1, 4(s0)
        ori    a1,a1,0x80
        sb     a1, 4(s0)
        andi   a1,a1,0x7F
        sb     a1, 4(s0) 
        jalr   x0, 0(ra)

        
        org 0x500
        dw     88
