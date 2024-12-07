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

    jump penasaran_1

label penasaran_1:
    window hide
    scene bg ruang_menjahit
    play sound "SFX/Kain.mp3" fadeout 1.3
    show mengamati at center
    play sound "SFX/Kain2.mp3" fadeout 1.3
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide mengamati

    show sriyani_muda at right
    with dissolve
    show larasati_kecil at left
    window show
    sriyani "[text_prolog_sriyani[6]]"

    window hide
    show berpikir at center
    with dissolve
    $renpy.pause(5.0, hard=True)
    hide berpikir
    window show

    show larasati_kecil at left
    with dissolve
    show sriyani_muda at right
    larasati "[text_prolog_larasati[6]]"

    hide larasati_kecil
    hide sriyani_muda
    window hide
    jump transisi_1

# ------ Chapter 1 ------
label transisi_1:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump chapter_1


label chapter_1:
    scene bg ruang_menjahit
    show larasatisma_senang at left
    with moveinleft
    with dissolve
    window show
    larasati "Aku pulang"
    show sriyanitua_bingung at right
    with dissolve
    sriyani "Pulang cepat hari ini kamu"
    larasati "Iya gurunya ada rapat jadi pulang lebih awal"
    hide sriyanitua_bingung
    show sriyanitua_senyum at right
    hide sriyanitua_senyum
    show sriyanitua_serius at right
    sriyani "Begitu"
    sriyani "kalau begitu kamu bisa melanjutkan desain motif batiknya"
    sriyani "Dan juga ada 2 kain yang harus kamu jadikan selendang hari ini"
    hide larasatisma_senang
    show larasatisma_kagetbiasa at left
    larasati "Bukannya aku sudah buat 4 desain kemarin ?"
    sriyani "Desainnya kurang menarik jika di aplikasikan ke kemeja"
    sriyani "Dan juga tidak cocok untuk diaplikasikan ke selendang"
    sriyani "Ibu kan sudah bilang untuk menggunakan motif yang sudah Ibu rekomendasikan"
    hide larasatisma_kagetbiasa
    show larasatisma_pasrah at left
    larasati "Bukannya yang ini bagus kalau jadi selendang"
    narrator "Larasati menunjuk jarinya ke arah desain motif yang sudah Ia buat"
    sriyani "Tidak nak, orangnya sudah bilang ke Ibu Dia tidak mau dengan desain motif seperti itu"
    sriyani "Kamu ini kenapa sih"
    sriyani "Kalau kamu tidak ada ide sendiri untuk membuat desain motif batik"
    sriyani "Gunakan desain yang sudah Ibu berikan"
    hide larasatisma_pasrah
    show larasatisma_murungsedih at left
    larasati "..."
    larasati "Iya bu"
    # 10:11
    narrator "Larasati membuat selendang pesanan orang"
    narrator "Membuat selendang cukup mudah untuknya"
    narrator "Karena sudah terbiasa sejak Ia masih anak-anak"
    # 12:20
    hide larasatisma_murungsedih
    hide sriyanitua_serius
    window hide
    jump transisi_2

label transisi_2:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump chapter_1_2

label chapter_1_2:
    show larasatisma_senang at center
    with moveinbottom
    with dissolve
    window show

    larasati "Selesai"
    larasati "Sekarang saatnya membuat desain motif batik"
    larasati "Apasih padahal desain motif ini bagus loh"
    hide larasatisma_senang
    show larasatisma_bingungheran at center
    larasati "Dan kenapa orangnya juga tidak suka ya"
    larasati "Ah malas sekali"
    larasati "Ide apa lagi yang bisa aku buat"
    narrator "Larasati melihat desain motif batik Ibunya yang sudah lama"
    narrator "Ada 3 desain motif batik"
    narrator "Tapi Larasati bosan melihat desain yang seperti itu dan ingin membuat desain yang lebih modern"
    narrator "Larasati tidak bisa mengerjakan desain motif batiknya"
    narrator "Karena pikiran yang tidak tenang"
    narrator "Ditambah harus belajar untuk ujian dua minggu lagi"
    hide larasatisma_bingungheran
    show larasatisma_bingungcemas at center
    larasati "Ah iya tugas sejarah belum selesai lagi"
    larasati "Mana sebentar lagi ujian"
    larasati "Bagaimana ini ?"
    larasati "Desain motif batik harus selesai dalam beberapa hari kedepan"
    narrator "Pikiran Larasati benar-benar kacau"
    narrator "Dia tidak bisa berpikir jernih untuk menyelesaikan masalahnya satu per satu"
    hide larasatisma_bingungcemas
    show larasatisma_murungsedih at center
    larasati "..."
    larasati "Kurang menarik"
    larasati "Yang ini kurang bagus"
    larasati "Ini warnanya..."
    larasati "Kalau desain ini dijadikan kemeja kayaknya aneh"
    narrator "Hampir 2 jam Larasati tidak menyelesaikan"
    # 14:35
    scene bg kamar_larasati
    narrator "Larasati belum menyelesaikan desainnya dan memilih untuk istirahat di kasur"
    hide larasatisma_murungsedih
    show larasatisma_bingungheran at center
    larasati "Haah..."
    larasati "Kenapa aku jadi tidak yakin begini ya dengan desain yang aku buat"
    narrator "Larasati memejamkan matanya"
    hide larasatisma_bingungheran
    window hide
    jump transisi_3

label transisi_3:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump chapter_1_3

label chapter_1_3:
    # sfx notif hp
    play sound "audio/SFX/Notif2.mp3" fadeout 1.0
    show larasatisma_kagetbiasa at center
    window show
    larasati "Siapa sih"
    hide larasatisma_kagetbiasa
    show larasatisma_senang at center
    with dissolve
    with moveinbottom
    larasati "Oh..."
    larasati "Rani"
    hide larasatisma_senang
    # gambar hp
    show phone at center:
        ypos 0.85
    rani "Sore ini kamu kosong gak ?"
    larasati "Kosong, memangnya kenapa ?"
    rani "Aku mau ngajak kamu ke kafe yang kemarin aku kasih tau"
    larasati "Ohh yang harganya mahal itu"
    rani "ENGGA MAHAL"
    larasati "Mana ada kopi harganya 25 ribu Ranii"
    rani "Ih, yaudah nanti aku tambahin"
    rani "Pokoknya nanti datang yahh, aku mau ngomong sesuatu"
    larasati "Kenapa gak bahas di WA aja?"
    rani "Nggak asik ah, enakan langsung ketemu sekalian minum kopi"
    larasati "Yaudah jam berapa"
    rani "Jam 15:30 kita disana"
    larasati "Okelah"
    hide phone

    # transisi -------------
    window hide
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    window show

    # 15:35
    scene bg cafe
    show rani_base at center
    with moveinleft
    narrator "Rani sudah sampai di kafe tapi Larasati belum datang"
    rani "..."
    rani "Ternyata belum sampai Dia"
    # 15:55
    rani "Lama banget sih itu anak"
    narrator "Larasati akhirnya datang"
    narrator "Rani melambaikan tangan untuk memberitahu Larasati"
    hide rani_base
    show rani_senang at right
    rani "Datang juga kamu"
    show larasati_casuall_senang at left
    with dissolve
    larasati "Ah iya"
    rani "Aku sampai pesan kopi duluan"
    rani "Kenapa lama sekali sih ?"
    hide larasati_casuall_senang
    show larasati_casuall_senyum at left
    larasati "Dih..."
    larasati "Macet tahu"
    rani "Dih..."
    rani "Alasan"
    larasati "Au ah"
    larasati "Aku mau pesan kopi dulu"
    narrator "Setelah Larasati memesan kopi"
    narrator "Mereka melanjutkan pembicaraan"
    hide larasati_casuall_senyum
    show larasati_casuall_pasrah at left
    larasati "Tempatnya lumayan juga"
    rani "Iyalah"
    larasati "Tapi lumayan mahal-mahal menunya"
    rani "Yaa standard harga kafe sih"
    rani "Ngomong-ngomong kemarin kamu lagi bikin desain motif batik ya ?"
    larasati "Iya"
    rani "Udah selesai ?"
    larasati "Sudah"
    larasati "Tapi aku harus buat ulang"
    rani "Loh"
    larasati "Desain yang aku buat ternyata nggak sesuai keinginan pelanggan"
    rani "Ooh"
    rani "Jadi kamu buat ulang lagi tuh ?"
    larasati "Iyalah"
    rani "Sudah selesai ?"
    hide larasati_casuall_pasrah
    show larasati_casuall_murungs at left
    larasati "Belum"
    larasati "Aku bingung nggak ada ide lagi"
    larasati "Eh udah sih tapi aku nggak yakin hasilnya bagus di manat orang lain"
    rani "Emang kamu bikin yang kaya gimana"
    hide larasati_casuall_murungs
    show larasati_casuall_pasrah at left
    larasati "Aku bikin yang modelnya agak modern gitu"
    larasati "Tapi kayaknya aneh kalau di aplikasikan ke kemeja"
    rani "Batik tapi modern ?"
    rani "Emang ada ya ?"
    larasati "Ada aku pernah lihat waktu liburan ke Solo"
    rani "Hmm aku nggak tahu banyak sih tentang batik"
    rani "Tapi kalau desain harusnya selera masing-masing orang"
    larasati "..."
    larasati "Iya sih aku harus membuat desain yang menarik menurut pandangan orang lain"
    rani "Kamu tidak menggunakan desain model dari Ayahmu ?"
    rani "Kamu pernah bilang dulu Ayahmu suka sekali membuat model batik kan?"
    larasati "Sudah"
    larasati "Aku sudah melihat semua buku gambarnya"
    larasati "Tapi aku cukup bosan melihat model yang begitu-begitu saja"
    larasati "Aku mau buat desain model batikku sendiri"
    rani "Memang susah sih kalau membuat desain sendiri"
    rani "Coba saja kamu cari buku-buku Ayahmu lagi"
    rani "Siapa tahu ada desain model batik yang dapat membantu kamu"
    larasati "Yaa nanti saja lah"
    larasati "Aku sedang tidak ingin mencari ide untuk desain"
    rani "Hmm"
    rani "Yaa tidak apa-apa"
    rani "Untuk mencari ide memang tidak harus terburu-buru"
    hide rani_senang
    hide larasati_casuall_pasrah
    show rani_ngodain at left
    show larasati_casuall_tertarik at left
    rani "Eh kamu tahu kakak kelas kita nggak yang ikut ekskul bahasa Inggris"
    larasati "Yang mana ? ada banyak tuh"
    rani "Itu yang namanya *bisik-bisik*"
    hide larasati_casuall_tertarik
    show larasati_casuall_senyum at left 
    larasati "Ohh diaaa"
    larasati "Dia kenapa ?"
    rani "Dia masih single tidak ya"
    larasati "Dih"
    larasati "Mau deketin anak orang"
    hide rani_ngodain
    show rani_jahil at right
    rani "Dih"
    rani "Suka-suka"
    larasati "Emang dia single ?"
    hide rani_jahil
    show rani_senyum at right
    rani "Harusnya sih iya"
    rani "Dia nggak pernah bikin status sama pasangannya sih"
    narrator "Obrolan mereka berlanjut sampai jam 19:45"
    narrator "Dan mereka pulang ke rumah masing-masing"

    window hide
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    window show

    larasati "Aku pulang"
    # 20:25
    narrator "Larasati sampai di rumah"
    narrator "Dan teringat harus bersih-bersih dan melanjutkan desainnya"
    sriyani "Baru pulang ?"
    sriyani "Sudah makan belum"
    sriyani "Nasi sama lauknya mau dimasukin ke lemari es"
    larasati "Sudah bu"
    sriyani "Oh yasudah"
    sriyani "Sebelum tidur mandi dulu"
    larasati "Baik bu"
    sriyani "Sama desainnya jangan lupa dikerjakan juga"
    larasati "..."
    larasati "Iya bu"
    narrator "Larasati pergi ke kamarnya"
    larasati "Huft..."
    larasati "Mandi ya"
    larasati "Malas mandi lagi"
    narrator "Larasati masih memikirkan desain model batiknya"
    narrator "Ia merasa bahwa desain modelnya masih kurang bagus"
    narrator "Larasati sekali lagi melihat desain model Ibunya"
    larasati "Ah, apa Ayah masih buku desain motif batik tidak ya"
    larasati "Tapi sudah aku baca semua sih buku yang Ayah kasih"
    larasati "Sudah lah mandi saja"
    narrator "Tapi Larasati tetap penasaran"
    narrator "Ada rasa ingin mencari buku peninggalan Ayahnya"
    larasati "Ih..."
    larasati "Kenapa aku jadi kepikiran begini"
    narrator "Dan akhirnya..."
    narrator "Larasati membuka semua lemari dan laci yang ada di kamarnya dan mencari buku peninggalan ayahnya"
    narrator "Larasati membuka laci yang ada di sebelah kasurnya"
    narrator "Ketika baru dibuka, tiba-tiba ada buku yang tidak pernah Ia lihat sebelumnya"
    larasati "Eh..."
    larasati "Sebentar"
    larasati "Ini buku apa ya"
    larasati "Belum pernah lihat"
    larasati "Dan siapa yang meletakkannya disini ?"
    larasati "Hmm..."
    larasati "Rahara Batik"
    larasati "Ini buku Ayah ?"
    narrator "Larasati membuka buku tersebut"
    narrator "Tiba-tiba ada cahaya yang muncul dari buku tersebut"
    larasati "Huaah..."
    narrator "Buku tersebut melayang di hadapan Larasati"
    larasati "Eh bukunya terbang"
    larasati "Eh kenapa jadi ada gempa begini ?"
    narrator "Barang-barang berjatuhan ke lantai"
    narrator "Suasana menjadi tegang seperti ada bencana yang datang"
    narrator "Dan Tiba-tiba Larasati masuk ke dalam buku tersebut"
    narrator "..."
    narrator "..."
    narrator "Semua menjadi hening"
    narrator "Buku yang Larasati pegang berada di tempat semula"
    narrator "Barang-barang yang berjatuhan kembali ke tempat semula"

    jump chapter_2

label chapter_2:
    "ch 2"