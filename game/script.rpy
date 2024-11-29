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
    stop music fadeout 1.3
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
    jump penasaran_1

label penasaran_1:
    scene envi_mom
    show mengamati at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mengamati

    show sriyani_muda at right
    with dissolve
    show larasati_kecil at left
    sriyani "[text_prolog_sriyani[6]]"

    scene envi_mom
    show berpikir at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide berpikir

    show larasati_kecil at left
    with dissolve
    show sriyani_muda at right
    larasati "[text_prolog_larasati[6]]"

    # This ends the game.
    hide larasati_kecil
    hide sriyani_muda
    jump kamar_larasati_1


label kamar_larasati_1:
    scene kamar_larasati
    show mencobaa at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencobaa
    show mencoba at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencoba

    show larasati_sma at left
    with dissolve

    larasati "[text_larasati_kamar[0]]"
    larasati "[text_larasati_kamar[1]]"

    scene kamar_larasati
    show kebingungan at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide kebingungan

    show larasati_sma at left
    larasati "[text_larasati_kamar[2]]"

    scene kamar_larasati
    show notif_pesan at center
    play sound "SFX/Notif2.mp3"
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide notif_pesan
    jump dm_dari_rani

label dm_dari_rani:
    scene kamar_larasati
    show phone at center
    with dissolve
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[0]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[0]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[1]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[1]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[2]]"
    play sound "audio/SFX/typing4.mp3" fadeout 1.5
    larasati "[text_larasati_dm[2]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[4]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[5]]"
    play sound "audio/SFX/typing2.mp3" fadeout 0.6
    larasati "[text_larasati_dm[4]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[6]]"
    play sound "audio/SFX/typing3.mp3" fadeout 0.7
    larasati "[text_larasati_dm[5]]"

    hide phone
    with dissolve
    jump kamar_larasati_2

label kamar_larasati_2:
    scene kamar_larasati
    show terdiam at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide terdiam

    show larasati_sma at center
    with dissolve

    larasati "[text_larasati_kamar[3]]"
    larasati "[text_larasati_kamar[4]]"
    jump dikafe_3


label dikafe_3:
    scene cafe
    show menunggu at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide menunggu

    scene cafe
    show rani_outfit at center
    with dissolve

    rani "[text_rani[7]]"
    rani "[text_rani[8]]"

    hide rani_outfit
    with dissolve

    scene cafe
    show ketemuan at center
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide ketemuan

    show rani_outfit at right
    with dissolve

    rani "[text_rani[9]]"

    show larasati_outfit at left
    with dissolve

    larasati "[text_larasati_kafe[0]]"
    rani "[text_rani[10]]"
    larasati "[text_larasati_kafe[1]]"
    larasati "[text_larasati_kafe[2]]"


    return
