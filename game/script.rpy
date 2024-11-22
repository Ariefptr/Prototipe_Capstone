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
    show larasati_sma at left:
        zoom 0.8 xalign 0.089 yalign 1.0
    with fade
    larasati "[text_prolog_larasati[0]]"
    show sriyani at right:
        zoom 0.17 xalign 0.94 yalign 2.0
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
    hide sriyani
    with dissolve
    larasati "[text_prolog_larasati[6]]"
    show sriyani at right:
        zoom 0.17 xalign 0.94 yalign 2.0
    with dissolve
    sriyani "[text_prolog_sriyani[6]]"

    larasati "[text_prolog_larasati[7]]"

    # This ends the game.

    return
