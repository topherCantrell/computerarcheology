
._CPU = 6809
._default_base_page = true

0x0000:

    LDA   <0x50  ; Force base page
    LDA   >0x50  ; Force direct
    LDA   0x50   ; Let the assembler choose
