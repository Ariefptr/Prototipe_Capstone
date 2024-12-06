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
    play music "BGM/All_Idle_Game_BGM.mp3" volume 0.7
    scene bg kamar_larasati
    narrator "[narator_text[0]]"
    show lolilaras_base at left
    with fade
    larasati "[text_prolog_larasati[0]]"
    larasati "[text_prolog_larasati[1]]"
    narrator "[narator_text[1]]"
    scene bg ruang_menjahit
    show sriyani_senyum at right
    show lolilaras_base at left
    with fade
    sriyani "[text_prolog_sriyani[0]]"
    larasati "[text_prolog_larasati[2]]"
    narrator "[narator_text[2]]"
    play sound "SFX/SFX_MesinJahit2.mp3" fadeout 1.3
    with dissolve
    larasati "[text_prolog_larasati[3]]"
    sriyani "[text_prolog_sriyani[1]]"
    sriyani "[text_prolog_sriyani[2]]"
    stop sound fadeout 0.5
    sriyani "[text_prolog_sriyani[3]]"
    larasati "[text_prolog_larasati[4]]"
    hide lolilaras_base
    with fade
    narrator "[narator_text[3]]"
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    show lolilaras_base at left
    with fade
    larasati "[text_prolog_larasati[5]]"
    sriyani "[text_prolog_sriyani[4]]"
    sriyani "[text_prolog_sriyani[5]]"
    narrator "[narator_text[4]]"
    larasati "[text_prolog_larasati[6]]"
    sriyani "[text_prolog_sriyani[6]]"
    larasati "[text_prolog_larasati[7]]"
    sriyani "[text_prolog_sriyani[7]]"
    larasati "[text_prolog_larasati[8]]"
    narrator "[narator_text[5]]"
    larasati "[text_prolog_larasati[9]]"
    larasati "[text_prolog_larasati[10]]"
    narrator "[narator_text[6]]"
    sriyani "[text_prolog_sriyani[8]]"
    narrator "[narator_text[7]]"
    hide lolilaras_base 
    hide sriyani_senyum
    with dissolve
    scene bg kamar_larasati
    show lolilaras_base
    with fade
    play sound "SFX/kertas.mp3" fadeout 1.3
    narrator "[narator_text[8]]"
    narrator "[narator_text[9]]"
    hide lolilaras_base
    with dissolve
    narrator "[narator_text[10]]"
    scene bg ruang_menjahit
    show lolilaras_bahagia at left
    show sriyani_senang at right
    with fade
    larasati "[text_prolog_larasati[11]]"
    narrator "[narator_text[11]]"
    sriyani "[text_prolog_sriyani[9]]"
    show lolilaras_senang at left
    show sriyani_ketawa at right
    narrator "[narator_text[12]]"
    hide lolilaras_senang
    hide sriyani_ketawa
    with dissolve
    scene bg ruang_menjahit
    with fade
    narrator "[narator_text[13]]"
    show lolilaras_base at left
    show sriyani_senyum at right
    with fade
    larasati "[text_prolog_larasati[12]]"
    play sound "SFX/SFX_MesinJahit2.mp3" fadeout 1.3
    with dissolve
    sriyani "[text_prolog_sriyani[10]]"
    larasati "[text_prolog_larasati[13]]"
    stop sound fadeout 0.5
    larasati "[text_prolog_larasati[14]]"
    sriyani "[text_prolog_sriyani[11]]"
    larasati "[text_prolog_larasati[15]]"
    narrator "[narator_text[14]]"
    narrator "[narator_text[15]]"
    show sriyani_ketawa at right
    narrator "[narator_text[16]]"
    show sriyani_ketawav2 at right
    larasati "[text_prolog_larasati[16]]"
    sriyani "[text_prolog_sriyani[12]]"
    sriyani "[text_prolog_sriyani[13]]"
    show lolilaras_penasaran at left
    larasati "[text_prolog_larasati[17]]"
    sriyani "[text_prolog_sriyani[14]]"
    sriyani "[text_prolog_sriyani[15]]"
    sriyani "[text_prolog_sriyani[16]]"
    larasati "[text_prolog_larasati[18]]"
    sriyani "[text_prolog_sriyani[17]]"
    show lolilaras_bahagia at left
    larasati "[text_prolog_larasati[19]]"
    larasati "[text_prolog_larasati[20]]"
    sriyani "[text_prolog_sriyani[18]]"
    larasati "[text_prolog_larasati[21]]"
    larasati "[text_prolog_larasati[22]]"
    sriyani "[text_prolog_sriyani[19]]"
    sriyani "[text_prolog_sriyani[20]]"
    show lolilaras_senang at left
    larasati "[text_prolog_larasati[23]]"
    larasati "[text_prolog_larasati[24]]"
    larasati "[text_prolog_larasati[25]]"
    hide sriyani_ketawav2 
    show sriyani_ketawa at right
    narrator "[narator_text[17]]"
    sriyani "[text_prolog_sriyani[21]]"
    larasati "[text_prolog_larasati[26]]"
    sriyani "[text_prolog_sriyani[22]]"
    larasati "[text_prolog_larasati[27]]"
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    narrator "[narator_text[18]]"
    play sound "SFX/Kain.mp3" fadeout 1.3
    with dissolve
    sriyani "[text_prolog_sriyani[23]]"
    sriyani "[text_prolog_sriyani[24]]"
    narrator "[narator_text[19]]"
    hide lolilaras_senang
    hide sriyani_ketawa
    with dissolve


    jump larasati_sudah_sma


label larasati_sudah_sma:
    scene bg kamar_larasati
    narrator "[text_narrator_sma[0]]"
    narrator "[text_narrator_sma[1]]"
    narrator "[text_narrator_sma[2]]"
    narrator "[text_narrator_sma[3]]"
    scene bg ruang_menjahit
    show larasatisma_senang at left
    with fade
    larasati "[text_larasati_sma[0]]"
    show sriyanitua_senyum at right
    with fade
    sriyani "[text_sriyani_sma[0]]"
    larasati "[text_larasati_sma[1]]"
    sriyani "[text_sriyani_sma[1]]"
    sriyani "[text_sriyani_sma[2]]"
    larasati "[text_larasati_sma[2]]"
    sriyani "[text_sriyani_sma[3]]"
    sriyani "[text_sriyani_sma[4]]"
    hide larasatisma_senang
    show larasatisma_bingungheran at left
    larasati "[text_larasati_sma[3]]"
    narrator "[text_narrator_sma[4]]"
    hide sriyanitua_senyum
    show sriyanitua_pasrah at right
    sriyani "[text_sriyani_sma[5]]"
    hide sriyanitua_pasrah
    show sriyanitua_bingung at right
    sriyani "[text_sriyani_sma[6]]"
    sriyani "[text_sriyani_sma[7]]"
    hide larasatisma_bingungheran
    show larasatisma_pasrah at left
    larasati "[text_larasati_sma[4]]"
    larasati "[text_larasati_sma[5]]"
    hide larasatisma_pasrah
    hide sriyanitua_bingung
    with dissolve
    show larasatisma_kalem
    with fade
    narrator "[text_narrator_sma[5]]"
    narrator "[text_narrator_sma[6]]"
    with dissolve
    scene bg kamar_larasati
    show larasatisma_senang 
    with fade
    larasati "[text_larasati_sma[6]]"
    larasati "[text_larasati_sma[7]]"
    hide larasatisma_senang
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[8]]"
    hide larasatisma_bingungcemas
    show larasatisma_murungsedih
    larasati "[text_larasati_sma[9]]"
    larasati "[text_larasati_sma[10]]"
    hide larasatisma_murungsedih
    show larasatisma_pasrah
    narrator "[text_narrator_sma[7]]"
    narrator "[text_narrator_sma[8]]"
    narrator "[text_narrator_sma[9]]"
    narrator "[text_narrator_sma[10]]"
    hide larasatisma_pasrah
    show larasatisma_kagetemoji
    larasati "[text_larasati_sma[11]]"
    larasati "[text_larasati_sma[12]]"
    hide larasatisma_kagetemoji
    show larasatisma_kagethoror
    larasati "[text_larasati_sma[13]]"
    hide larasatisma_kagethoror
    show larasatisma_kagetemoji2
    narrator "[text_narrator_sma[11]]"
    narrator "[text_narrator_sma[12]]"
    hide larasatisma_kagetemoji2
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[14]]"
    larasati "[text_larasati_sma[15]]"
    larasati "[text_larasati_sma[16]]"
    larasati "[text_larasati_sma[17]]"
    larasati "[text_larasati_sma[18]]"
    hide larasatisma_bingungcemas
    show larasatisma_pasrah
    larasati "[text_larasati_sma[19]]"
    narrator "[text_narrator_sma[13]]"
    hide larasatisma_pasrah
    show larasatisma_bingungcemas
    larasati "[text_larasati_sma[20]]"
    hide larasatisma_bingungcemas
    narrator "[text_narrator_sma[14]]"




# label penasaran_1:
#     scene envi_mom
#     play sound "SFX/Kain.mp3" fadeout 1.3
#     show mengamati at center
#     play sound "SFX/Kain2.mp3" fadeout 1.3
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide mengamati

#     show sriyani_muda at right
#     with dissolve
#     show larasati_kecil at left
#     sriyani "[text_prolog_sriyani[6]]"

#     scene envi_mom
#     show berpikir at center
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide berpikir

#     show larasati_kecil at left
#     with dissolve
#     show sriyani_muda at right
#     larasati "[text_prolog_larasati[6]]"

#     # This ends the game.
#     hide larasati_kecil
#     hide sriyani_muda
#     jump kamar_larasati_1


# label kamar_larasati_1:
#     scene kamar_larasati
#     show mencobaa at center
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide mencobaa
#     show mencoba at center
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide mencoba

#     show larasati_sma at left
#     with dissolve

#     larasati "[text_larasati_kamar[0]]"
#     larasati "[text_larasati_kamar[1]]"

#     scene kamar_larasati
#     show kebingungan at center
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide kebingungan

#     show larasati_sma at left
#     larasati "[text_larasati_kamar[2]]"

#     scene kamar_larasati
#     show notif_pesan at center
#     play sound "SFX/Notif2.mp3"
#     with dissolve
#     $renpy.pause(4.0, hard=True)
#     hide notif_pesan
#     jump dm_dari_rani

label dm_dari_rani:
    scene kamar_larasati
    show phone at center
    with dissolve
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    larasati "[text_larasati_dm[0]]"
    rani "[text_rani[0]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[1]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[1]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[2]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[2]]"
    play sound "audio/SFX/typing4.mp3" fadeout 1.5
    larasati "[text_larasati_dm[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[3]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[4]]"
    play sound "audio/SFX/typing.mp3" fadeout 1.5
    larasati "[text_larasati_dm[4]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[5]]"
    play sound "audio/SFX/typing2.mp3" fadeout 0.6
    larasati "[text_larasati_dm[5]]"
    play sound "audio/SFX/dring.mp3" fadeout 0.3
    rani "[text_rani[6]]"
    play sound "audio/SFX/typing3.mp3" fadeout 0.7
    larasati "[text_larasati_dm[6]]"

    hide phone
    with dissolve
    jump kafe_sore

label kafe_sore:
    scene cafe
    with dissolve
    narrator "[text_narrator_kafe[0]]"
    narrator "[text_narrator_kafe[1]]"
    show rani_base 
    rani "[text_rani_kafe[0]]"
    hide rani_base
    narrator "[text_narrator_kafe[2]]"
    show rani_base
    rani "[text_rani_kafe[1]]"
    play sound "audio/SFX/SFX_Bell.mp3" fadeout 0.5
    narrator "[text_narrator_kafe[3]]"
    hide rani_base
    show rani_seyumciptadent
    narrator "[text_narrator_kafe[4]]"
    hide rani_seyumciptadent
    show rani_base at right
    with fade
    rani "[text_rani_kafe[2]]"
    show larasati_senyum at left
    with dissolve
    larasati "[text_larasati_kafe[0]]"
    rani "[text_rani_kafe[3]]"
    rani "[text_rani_kafe[4]]"
    hide larasati_senyum
    show larasati_bingungheran at left
    larasati "[text_larasati_kafe[1]]"
    hide rani_base
    show rani_ngodain at right
    rani "[text_rani_kafe[5]]"
    hide larasati_bingungheran
    show larasati_pasrah at left
    larasati "[text_larasati_kafe[2]]"
    narrator "[text_narrator_kafe[5]]"
    with fade
    hide larasati_pasrah
    show larasati_senyum at left
    larasati "[text_larasati_kafe[3]]"
    hide rani_ngodain
    show rani_base at right
    rani "[text_rani_kafe[6]]"
    larasati "[text_larasati_kafe[4]]"
    rani "[text_rani_kafe[7]]"
    rani "[text_rani_kafe[8]]"
    larasati "[text_larasati_kafe[5]]"
    rani "[text_rani_kafe[9]]"
    larasati "[text_larasati_kafe[6]]"
    rani "[text_rani_kafe[10]]"
    larasati "[text_larasati_kafe[7]]"
    rani "[text_rani_kafe[11]]"
    larasati "[text_larasati_kafe[8]]"
    rani "[text_rani_kafe[12]]"
    larasati "[text_larasati_kafe[9]]"
    larasati "[text_larasati_kafe[10]]"
    rani "[text_rani_kafe[13]]"
    larasati "[text_larasati_kafe[11]]"
    rani "[text_rani_kafe[14]]"
    larasati "[text_larasati_kafe[12]]"
    rani "[text_rani_kafe[15]]"
    rani "[text_rani_kafe[16]]"
    larasati "[text_larasati_kafe[13]]"
    larasati "[text_larasati_kafe[14]]"
    rani "[text_rani_kafe[17]]"
    rani "[text_rani_kafe[18]]"
    larasati "[text_larasati_kafe[15]]"
    larasati "[text_larasati_kafe[16]]"
    larasati "[text_larasati_kafe[17]]"
    rani "[text_rani_kafe[19]]"
    rani "[text_rani_kafe[20]]"
    rani "[text_rani_kafe[21]]"
    larasati "[text_larasati_kafe[18]]"
    rani "[text_rani_kafe[22]]"
    rani "[text_rani_kafe[23]]"
    rani "[text_rani_kafe[24]]"
    larasati "[text_larasati_kafe[19]]"
    rani "[text_rani_kafe[25]]"
    larasati "[text_larasati_kafe[20]]"
    rani "[text_rani_kafe[26]]"
    larasati "[text_larasati_kafe[21]]"
    rani "[text_rani_kafe[27]]"
    larasati "[text_larasati_kafe[22]]"
    rani "[text_rani_kafe[28]]"
    narrator "[text_narrator_kafe[6]]"
    hide larasati_senyum 
    hide rani_base
    with fade
    narrator "[text_narrator_kafe[7]]"
    with dissolve


    jump pulang_rumah

label pulang_rumah:
    scene bg ruang_menjahit
    show larasati_kalem
    with fade
    larasati "[text_larasati_pulangkafe[0]]"
    narrator "[text_narrator_pulang[0]]"
    narrator "[text_narrator_pulang[1]]"
    narrator "[text_narrator_pulang[2]]"
    hide larasati_kalem 
    show sriyanitua_tulus at right
    show larasati_senyum at left
    sriyani "[text_respon_ibularas[0]]"
    sriyani "[text_respon_ibularas[1]]"
    larasati "[text_larasati_pulangkafe[1]]"
    sriyani "[text_respon_ibularas[2]]"
    larasati "[text_larasati_pulangkafe[2]]"
    sriyani "[text_respon_ibularas[3]]"
    larasati "[text_larasati_pulangkafe[3]]"
    larasati "[text_larasati_pulangkafe[4]]"
    narrator "[text_narrator_pulang[3]]"
    hide sriyanitua_tulus
    hide larasati_senyum 
    with dissolve
    scene bg kamar_larasatimalam
    show larasati_pasrah
    larasati "[text_larasati_pulangkafe[5]]"
    larasati "[text_larasati_pulangkafe[6]]"
    larasati "[text_larasati_pulangkafe[7]]"
    narrator "[text_narrator_pulang[4]]"
    narrator "[text_narrator_pulang[5]]"
    narrator "[text_narrator_pulang[6]]"
    hide larasati_pasrah
    show larasati_bingungcemas
    larasati "[text_larasati_pulangkafe[8]]"
    larasati "[text_larasati_pulangkafe[9]]"
    hide larasati_bingungcemas
    show larasati_pasrah
    larasati "[text_larasati_pulangkafe[10]]"
    narrator "[text_narrator_pulang[7]]"
    narrator "[text_narrator_pulang[8]]"
    larasati "[text_larasati_pulangkafe[11]]"
    hide larasati_pasrah
    narrator "[text_narrator_pulang[9]]"
    narrator "[text_narrator_pulang[10]]"
    narrator "[text_narrator_pulang[11]]"
    show larasati_bingungcemas
    narrator "[text_narrator_pulang[12]]"
    larasati "[text_larasati_pulangkafe[12]]"
    larasati "[text_larasati_pulangkafe[13]]"
    larasati "[text_larasati_pulangkafe[14]]"
    larasati "[text_larasati_pulangkafe[15]]"
    narrator "[text_narrator_pulang[13]]"
    narrator "[text_narrator_pulang[14]]"
    hide larasati_bingungcemas
    show larasati_kagetemoji1
    larasati "[text_larasati_pulangkafe[16]]"
    narrator "[text_narrator_pulang[15]]"
    hide larasati_kagetemoji1
    show larasati_kagetemoji2
    larasati "[text_larasati_pulangkafe[17]]"
    larasati "[text_larasati_pulangkafe[18]]"
    narrator "[text_narrator_pulang[16]]"
    narrator "[text_narrator_pulang[17]]"
    narrator "[text_narrator_pulang[18]]"
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi
    hide larasati_kagetemoji2
    narrator "[text_narrator_pulang[19]]"
    narrator "[text_narrator_pulang[20]]"
    narrator "[text_narrator_pulang[21]]"


# label dikafe_3:
#     scene cafe
#     show menunggu at center
#     with dissolve
#     $renpy.pause(5.0, hard=True)
#     hide menunggu

#     scene cafe
#     show rani_outfit at center
#     with dissolve

#     rani "[text_rani[7]]"
#     rani "[text_rani[8]]"

#     hide rani_outfit
#     with dissolve

#     scene cafe
#     show ketemuan at center
#     with dissolve
#     $renpy.pause(6.0, hard=True)
#     hide ketemuan

#     show rani_outfit at right
#     with dissolve

#     rani "[text_rani[9]]"

#     show larasati_outfit at left
#     with dissolve

#     larasati "[text_larasati_kafe[0]]"
#     rani "[text_rani[10]]"
#     larasati "[text_larasati_kafe[1]]"
#     larasati "[text_larasati_kafe[2]]"

#     scene cafe
#     show screen white_screen
#     with dissolve
#     $renpy.pause(3.0, hard=True)
#     hide screen white_screen
#     scene cafe
#     show screen black_screen
#     with dissolve
#     $renpy.pause(3.0, hard=True)
#     hide screen black_screen
#     jump dunia_lain

label dunia_lain:
    show dimensi
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi
    jump story_parang

label story_parang:
    scene hutan_parang
    show dimensi_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide dimensi_1

    scene hutan_parang
    with dissolve
    larasati "[larasati_story_2[0]]"

    scene hutan_parang
    show terbangun
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide terbangun
    show mengingat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide mengingat

    show larasati_outfit at center
    with dissolve

    larasati "[larasati_story_2[1]]"
    larasati "[larasati_story_2[2]]"
    larasati "[larasati_story_2[3]]"
    larasati "[larasati_story_2[4]]"
    larasati "[larasati_story_2[5]]"
    scene hutan_parang
    show tenang
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide tenang
    show melihat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[6]]"
    larasati "[larasati_story_2[7]]"
    larasati "[larasati_story_2[8]]"
    larasati "[larasati_story_2[9]]"
    larasati "[larasati_story_2[10]]"
    larasati "[larasati_story_2[11]]"

    scene hutan_parang
    show keliling
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide keliling

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[12]]"
    larasati "[larasati_story_2[13]]"
    larasati "[larasati_story_2[14]]"
    larasati "[larasati_story_2[15]]"
    larasati "[larasati_story_2[16]]"
    larasati "[larasati_story_2[17]]"
    larasati "[larasati_story_2[18]]"

    scene hutan_parang
    show keliling_1
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide keliling_1
    show keliling_2
    with dissolve
    $renpy.pause(11.0, hard=True)
    hide keliling_2

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[19]]"
    larasati "[larasati_story_2[20]]"

    scene hutan_parang
    show mencari
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mencari

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[21]]"

    scene hutan_parang
    show pikiran
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide pikiran

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[22]]"
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve

    scene hutan_parang
    show tinggal
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide tinggal
    show melihat_1
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide melihat_1

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[23]]"
    show misterius at right:
        zoom 1.74
        xpos 1279 ypos 524
    with dissolve
    larasati "[larasati_story_2[24]]"
    larasati "[larasati_story_2[25]]"

    scene hutan_parang
    show waspada
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide waspada
    show waspada_1
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide waspada_1

    show larasati_outfit at left
    with dissolve
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit_1 at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide misterius
    with dissolve
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    hide larasati_outfit
    with dissolve

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[26]]"

    show makara at right
    with dissolve
    makhluk "[suara_misterius[0]]"
    larasati "[larasati_story_2[27]]"
    scene hutan_parang
    show terkaget
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide terkaget

    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[28]]"
    scene hutan_parang
    show penasaran
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide penasaran
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[29]]"
    show makara at right
    with dissolve
    makhluk "[suara_misterius[1]]"
    scene hutan_parang
    show tenang_1
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide tenang_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    show larasati_outfit at left
    makhluk "[suara_misterius[2]]"
    makhluk "[suara_misterius[3]]"
    makhluk "[suara_misterius[4]]"
    larasati "[larasati_story_2[30]]"
    larasati "[larasati_story_2[31]]"
    makhluk "[suara_misterius[5]]"
    scene hutan_parang
    show bicara
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide bicara
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk "[suara_misterius[6]]"
    larasati "[larasati_story_2[32]]"
    larasati "[larasati_story_2[33]]"
    makhluk "[suara_misterius[7]]"
    larasati "[larasati_story_2[34]]"
    makhluk "[suara_misterius[8]]"
    larasati "[larasati_story_2[35]]"
    makhluk_1 "[text_makara[0]]"
    makhluk_1 "[text_makara[1]]"
    larasati "[larasati_story_2[36]]"
    larasati "[larasati_story_2[37]]"

    scene hutan_parang
    show notis
    with dissolve
    $renpy.pause(10.0, hard=True)
    hide notis
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[2]]"
    makhluk_1 "[text_makara[3]]"
    larasati "[larasati_story_2[38]]"
    larasati "[larasati_story_2[39]]"
    makhluk_1 "[text_makara[4]]"
    makhluk_1 "[text_makara[5]]"
    larasati "[larasati_story_2[40]]"
    makhluk_1 "[text_makara[6]]"
    makhluk_1 "[text_makara[7]]"
    makhluk_1 "[text_makara[8]]"
    makhluk_1 "[text_makara[9]]"
    scene hutan_parang
    show menjelaskan
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide menjelaskan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[10]]"
    larasati "[larasati_story_2[41]]"
    larasati "[larasati_story_2[42]]"
    makhluk_1 "[text_makara[11]]"
    makhluk_1 "[text_makara[12]]"
    makhluk_1 "[text_makara[13]]"
    larasati "[larasati_story_2[43]]"
    makhluk_1 "[text_makara[14]]"

    scene hutan_parang
    show mencari_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide mencari_1
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[44]]"
    larasati "[larasati_story_2[45]]"
    makhluk_1 "[text_makara[15]]"
    larasati "[larasati_story_2[46]]"
    makhluk_1 "[text_makara[16]]"
    scene hutan_parang
    show senang
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide senang
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[17]]"
    makhluk_1 "[text_makara[18]]"
    larasati "[larasati_story_2[47]]"
    scene hutan_parang
    show keliling_3
    with dissolve
    $renpy.pause(12.0, hard=True)
    hide keliling_3

    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[48]]"
    scene hutan_parang
    show tersenyum
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide tersenyum
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[19]]"
    makhluk_1 "[text_makara[20]]"
    hide makara
    show makara1 at right
    with dissolve
    hide makara1
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve

    scene hutan_parang
    show berjalan
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide berjalan

    scene hutan_parang
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[21]]"
    larasati "[larasati_story_2[49]]"
    makhluk_1 "[text_makara[22]]"
    larasati "[larasati_story_2[50]]"
    larasati "[larasati_story_2[51]]"
    makhluk_1 "[text_makara[23]]"
    larasati "[larasati_story_2[52]]"
    larasati "[larasati_story_2[53]]"
    larasati "[larasati_story_2[54]]"
    larasati "[larasati_story_2[55]]"
    larasati "[larasati_story_2[56]]"
    scene hutan_parang
    show menjelaskan_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide menjelaskan_1
    show memahami
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide memahami

    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[24]]"
    makhluk_1 "[text_makara[25]]"
    makhluk_1 "[text_makara[26]]"
    larasati "[larasati_story_2[57]]"
    makhluk_1 "[text_makara[27]]"
    makhluk_1 "[text_makara[28]]"
    scene hutan_parang
    show mengepakkan
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide mengepakkan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[58]]"
    larasati "[larasati_story_2[59]]"
    makhluk_1 "[text_makara[29]]"
    larasati "[larasati_story_2[60]]"
    scene hutan_parang
    show melanjutkan
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide melanjutkan
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    larasati "[larasati_story_2[61]]"
    larasati "[larasati_story_2[62]]"
    makhluk_1 "[text_makara[30]]"
    scene hutan_parang
    show melihat_2
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat_2
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[31]]"
    scene hutan_parang
    show melompat
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melompat
    show makara at right
    with dissolve
    hide makara
    show makara1 at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[32]]"
    hide makara1
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    with dissolve
    scene hutan_parang
    show melompat_1
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide melompat_1
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    hide larasati_outfit
    with dissolve
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    larasati "[larasati_story_2[63]]"
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[33]]"
    makhluk_1 "[text_makara[34]]"
    makhluk_1 "[text_makara[35]]"
    scene hutan_parang
    show menyadari
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide menyadari

    show larasati_outfit at center
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[64]]"
    scene hutan_parang
    show mengikuti
    with dissolve
    $renpy.pause(13.0, hard=True)
    hide mengikuti
    show melewati
    with dissolve
    $renpy.pause(6.0, hard=True)
    hide melewati
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit

    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[65]]"
    larasati "[larasati_story_2[66]]"
    makhluk_1 "[text_makara[36]]"
    makhluk_1 "[text_makara[37]]"
    makhluk_1 "[text_makara[38]]"
    makhluk_1 "[text_makara[39]]"
    scene hutan_parang
    show melihat_3
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide melihat_3
    scene hutan_parang
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[67]]"
    larasati "[larasati_story_2[68]]"
    larasati "[larasati_story_2[69]]"
    makhluk_1 "[text_makara[40]]"
    makhluk_1 "[text_makara[41]]"
    scene hutan_parang
    show makara1 at right
    with dissolve
    hide makara1
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at right
    with dissolve 
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show melanjutkan_1
    with dissolve
    $renpy.pause(9.0, hard=True)
    hide melanjutkan_1
    show keberanian
    with dissolve
    $renpy.pause(7.0, hard=True)
    hide keberanian

    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[42]]"
    makhluk_1 "[text_makara[43]]"
    scene hutan_parang
    show memahami_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide memahami_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[70]]"
    larasati "[larasati_story_2[71]]"
    larasati "[larasati_story_2[72]]"
    scene hutan_parang
    show senang_1
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide senang_1
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    makhluk_1 "[text_makara[44]]"
    scene hutan_parang
    show mengerti
    with dissolve
    $renpy.pause(10.0, hard=True)
    hide mengerti

    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[73]]"
    larasati "[larasati_story_2[74]]"
    makhluk_1 "[text_makara[45]]"
    hide makara
    scene hutan_parang
    show makara1 at right
    with dissolve
    $renpy.pause(1.0, hard=True)
    hide makara1
    scene hutan_parang
    show larasati_outfit at center
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show larasati_outfit at right
    with dissolve
    $renpy.pause(2.0, hard=True)
    hide larasati_outfit
    scene hutan_parang
    show setelah
    with dissolve
    $renpy.pause(3.0, hard=True)
    hide setelah
    scene bukit
    with dissolve
    show makara at right
    with dissolve
    show larasati_outfit at left
    with dissolve
    makhluk_1 "[text_makara[46]]"
    makhluk_1 "[text_makara[47]]"
    scene bukit
    show rebahan
    with dissolve
    $renpy.pause(4.0, hard=True)
    hide rebahan
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[75]]"
    larasati "[larasati_story_2[76]]"
    makhluk_1 "[text_makara[48]]"
    scene bukit
    show rebahan_1
    with dissolve
    $renpy.pause(11.0, hard=True)
    hide rebahan_1
    show menggambar
    with dissolve
    $renpy.pause(12.0, hard=True)
    hide menggambar
    show larasati_outfit at left
    with dissolve
    show makara at right
    with dissolve
    larasati "[larasati_story_2[77]]"
    larasati "[larasati_story_2[78]]"
    larasati "[larasati_story_2[79]]"

    hide larasati_outfit
    hide makara
    jump puzzle_rotate

label puzzle_rotate:
    call screen rotate_batik

label puzzle_rotate_2:
    call screen rotate_batik_2

label puzzle_rotate_3:
    call screen rotate_batik_3

label reward_puzzle:
    call screen reward_puzzle_1

label story_3:
    "story 3"
    
    return
