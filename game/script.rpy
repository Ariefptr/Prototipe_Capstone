style screentext:
    color "#f29c2cff"
    size 16
# The game starts here.

label start:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump prolog_pertama


label prolog_pertama:
    scene envi_mom
    show larasati_kecil at left
    with fade
    larasati "[text_prolog_larasati[0]]"
    show sriyani_muda at right
    with dissolve
    sriyani "[text_prolog_sriyani[0]]"

    larasati "[text_prolog_larasati[1]]"

    sriyani "[text_prolog_sriyani[1]]"

    larasati "[text_prolog_larasati[2]]"

    sriyani "[text_prolog_sriyani[2]]"

    larasati "[text_prolog_larasati[3]]"

    sriyani "[text_prolog_sriyani[3]]"

    larasati "[text_prolog_larasati[4]]"

    sriyani "[text_prolog_sriyani[4]]"

    larasati "[text_prolog_larasati[5]]"

    sriyani "[text_prolog_sriyani[5]]"
    hide sriyani_muda
    with dissolve
    larasati "[text_prolog_larasati[6]]"
    show sriyani_muda at right
    with dissolve
    sriyani "[text_prolog_sriyani[6]]"

    larasati "[text_prolog_larasati[7]]"

    # This ends the game prolog.
    hide larasati_kecil
    hide sriyani_muda
    jump kamar_larasati_1


label kamar_larasati_1:
    scene kamar_larasati 
    show larasati_sma at left 
    with dissolve

    larasati "[text_larasati_kamar[0]]"
    larasati "[text_larasati_kamar[1]]"
    larasati "[text_larasati_kamar[2]]"

    hide larasati_sma
    with dissolve
    jump dm_from_rani

label dm_from_rani:
    scene kamar_larasati
    show phone at center 
    with dissolve

    rani "[text_rani[0]]"
    larasati "[text_larasati_dm[0]]"
    rani "[text_rani[1]]"
    larasati "[text_larasati_dm[1]]"
    rani "[text_rani[2]]"
    larasati "[text_larasati_dm[2]]"
    rani "[text_rani[3]]"
    rani "[text_rani[4]]"
    larasati "[text_larasati_dm[3]]"
    rani "[text_rani[5]]"
    larasati "[text_larasati_dm[4]]"
    rani "[text_rani[6]]"
    larasati "[text_larasati_dm[5]]"

    hide phone 
    with dissolve
    jump kamar_larasati_2

label kamar_larasati_2:
    scene kamar_larasati
    show larasati_sma at center 
    with dissolve

    larasati "[text_larasati_kamar[3]]"
    larasati "[text_larasati_kamar[4]]"
