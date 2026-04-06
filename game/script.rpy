##############################################################
#  UNDANGAN PALSU — Ren'Py Visual Novel Script
#  Revisi: Ukuran karakter & HP diperbesar, karakter selalu muncul saat dialog
##############################################################

# ─────────────────────────────────────────
# DEKLARASI BACKGROUND
# ─────────────────────────────────────────
image bg_kamar_coding  = Transform("images/office1.jpg",   fit="cover")
image bg_hp_whatsapp   = Transform("images/topfloor.jpg",  fit="cover")
image bg_hp_call       = Transform("images/office2.jpg",   fit="cover")
image bg_laptop_screen = Transform("images/email.jpg",     fit="cover")
image bg_hacked        = Transform("images/window.jpg",    fit="cover")
image bg_kamar_gelap   = Transform("images/station.jpg",   fit="cover")
image bg_aman          = Transform("images/london.jpg",    fit="cover")
image bg_keluarga      = Transform("images/park1.jpg",     fit="cover")

# ─────────────────────────────────────────
# DEKLARASI SPRITE KARAKTER
# ─────────────────────────────────────────
image ibu_panik = Transform("images/Rai_serious.png", zoom=2.0)
image ibu_lega  = Transform("images/Rai.png", zoom=2.0)
image aku_foto  = Transform("images/Reg.png", zoom=2.0)
image ibu_foto  = Transform("images/Rai.png", zoom=2.0)

image hp_ibu = Transform("images/phonemother.png", zoom=0.65)
image hp_aku = Transform("images/phonemee.png",    zoom=0.2)

# ─────────────────────────────────────────
# TRANSFORMS — PHONE
# ─────────────────────────────────────────

# Masuk dari kanan (tunggal)
transform phone_enter_right:
    alpha 0.0
    xalign 1.25
    yalign 0.72
    easein 0.45 alpha 1.0 xalign 0.78

# Masuk dari kiri (tunggal)
transform phone_enter_left:
    alpha 0.0
    xalign -0.35
    yalign 0.72
    rotate -4
    easein 0.45 alpha 1.0 xalign 0.20 rotate 0

# Dua HP berjauhan — kiri (hp aku)
transform phone_enter_dual_left:
    alpha 0.0
    xalign -0.50
    yalign 0.60
    rotate -6
    easein 0.50 alpha 1.0 xalign 0.05 rotate 0

# Dua HP berjauhan — kanan (hp ibu)
transform phone_enter_dual_right:
    alpha 0.0
    xalign 1.50
    yalign 0.60
    rotate 6
    easein 0.50 alpha 1.0 xalign 0.95 rotate 0

# Muncul dari bawah (alert / notifikasi)
transform phone_enter_bottom_alert:
    alpha 0.0
    xalign 0.50
    yalign 1.35
    zoom 0.75
    easein 0.28 alpha 1.0 yalign 0.78 zoom 0.90
    linear 0.08 yalign 0.75
    linear 0.08 yalign 0.78

# Idle di posisi kanan
transform phone_idle:
    xalign 0.78
    yalign 0.72
    alpha 1.0

# ─────────────────────────────────────────
# TRANSFORMS — KARAKTER (diperbesar)
# ─────────────────────────────────────────

# Karakter sendirian di tengah
transform char_center:
    xalign 0.5
    yalign 1.0
    yoffset -10
    zoom 1.0
    alpha 1.0
    blur 0.0

# Posisi pasif kiri/kanan (2-shot)
transform char_left:
    xalign 0.15
    yalign 1.0
    yoffset -10
    zoom 0.88
    alpha 0.90
    blur 0.5

transform char_right:
    xalign 0.85
    yalign 1.0
    yoffset -10
    zoom 0.88
    alpha 0.90
    blur 0.5

# Karakter sedang berbicara (aktif)
transform char_active_center:
    xalign 0.5
    yalign 1.0
    yoffset -10
    zoom 1.0
    alpha 1.0
    blur 0.0
    matrixcolor BrightnessMatrix(0.0)
    linear 0.12 zoom 1.02

transform char_active_left:
    xalign 0.15
    yalign 1.0
    yoffset -10
    zoom 0.94
    alpha 1.0
    blur 0.0
    matrixcolor BrightnessMatrix(0.0)
    linear 0.12 zoom 0.96

transform char_active_right:
    xalign 0.85
    yalign 1.0
    yoffset -10
    zoom 0.94
    alpha 1.0
    blur 0.0
    matrixcolor BrightnessMatrix(0.0)
    linear 0.12 zoom 0.96

# Karakter diam (pasif) — lebih gelap & sedikit blur
transform char_passive_left:
    xalign 0.15
    yalign 1.0
    yoffset -10
    zoom 0.84
    alpha 0.75
    blur 1.0
    matrixcolor BrightnessMatrix(-0.25)

transform char_passive_right:
    xalign 0.85
    yalign 1.0
    yoffset -10
    zoom 0.84
    alpha 0.75
    blur 1.0
    matrixcolor BrightnessMatrix(-0.25)

# ─────────────────────────────────────────
# DEFINISI KARAKTER
# ─────────────────────────────────────────
define aku      = Character('Aku',      color="#3498db")
define ibu      = Character('Ibu',      color="#e74c3c")
define sistem   = Character('Terminal', color="#2ecc71")
define aku_chat = Character('Aku',      color="#3498db")
define ibu_chat = Character('Ibu',      color="#e74c3c")

# ─────────────────────────────────────────
# VARIABEL AWAL (FSM State Data)
# ─────────────────────────────────────────
default bukti_terkumpul          = 0
default ibu_paham                = False
default pengirim_terverifikasi   = False
default analisis_statis_selesai  = False
default analisis_dinamis_selesai = False


##############################################################
#  STATE 01 — START (Konflik Awal)
##############################################################
label start:
    scene bg_kamar_coding
    play music "audio/park.mp3" loop fadein 1.0

    show aku_foto at char_active_center with dissolve
    "Malam ini aku sedang sibuk menatap layar laptop ASUS TUF kesayanganku,\nmengejar deadline project mobile programming."

    play sound "audio/phone.wav"
    "Tiba-tiba layar iPhone-ku menyala. Ada pesan WhatsApp dari Ibu."
    hide aku_foto

    # ── Scene: chat WhatsApp ──────────────────────────────
    scene bg_hp_whatsapp
    play sound "audio/gulp.wav"

    show hp_aku  at phone_enter_dual_left
    show hp_ibu  at phone_enter_dual_right
    show aku_foto   at char_passive_left  with dissolve
    show ibu_foto   at char_active_right  with dissolve

    ibu_chat "Nak, ini ada undangan pernikahan dari kerabat jauh.\nTapi bentuknya aneh, tulisannya 'Undangan_Resmi.apk'."
    ibu_chat "Ibu klik ya biar bisa lihat lokasi gedungnya?"

    show aku_foto at char_active_left   with dissolve
    show ibu_foto at char_passive_right with dissolve
    aku_chat "Waduh! Bahaya ini. Itu jelas modus penipuan."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_foto

    # ── Kembali ke kamar ─────────────────────────────────
    scene bg_kamar_coding
    show aku_foto at char_active_center with dissolve
    "Masalahnya, orang tua sering kali tetap penasaran dan diam-diam mengeklik\nbila dilarang tanpa penjelasan yang masuk akal."
    hide aku_foto

    menu:
        "Larangan Biasa — 'Jangan diklik Bu, itu penipuan. Hapus aja.'":
            jump state_03_ignore

        "Investigasi — 'STOP BU! Jangan diklik. Kirim filenya ke aku, biar aku bongkar isinya.'":
            jump state_02_investigate


##############################################################
#  STATE 03 — IGNORE (Cabang Tunda / Malas)
##############################################################
label state_03_ignore:
    scene bg_hp_whatsapp
    play sound "audio/gulp.wav"

    show hp_aku  at phone_enter_dual_left
    show hp_ibu  at phone_enter_dual_right
    show aku_foto   at char_active_left   with dissolve
    show ibu_foto   at char_passive_right with dissolve

    aku_chat "Udah, Ibu jangan klik apa-apa. Hapus aja pesannya."

    show aku_foto at char_passive_left  with dissolve
    show ibu_foto at char_active_right  with dissolve
    ibu_chat "Oh, gitu ya. Ya sudah."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_foto

    scene bg_kamar_coding
    show aku_foto at char_active_center with dissolve
    "Aku kembali fokus ngoding, merasa masalah sudah selesai."
    "Namun, 30 menit kemudian..."
    hide aku_foto

    play sound "audio/sfx_phone_ring.ogg"
    play sound "audio/sfx_error.ogg"

    show hp_ibu at phone_enter_bottom_alert
    "Notifikasi darurat memenuhi layar: {i}Transaksi mencurigakan terdeteksi{/i}."
    hide hp_ibu

    # ── Telepon panik dari Ibu ───────────────────────────
    scene bg_hp_call
    play sound "audio/gulp.wav"

    show hp_aku    at phone_enter_dual_left
    show hp_ibu    at phone_enter_dual_right
    show aku_foto  at char_passive_left  with dissolve
    show ibu_panik at char_active_right  with dissolve

    ibu "Nak... uang di rekening Ibu kok tiba-tiba habis sisa nol?\nTadi orangnya nge-chat lagi, katanya kalau nggak di-klik bakal kena denda.\nJadi Ibu klik..."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_panik

    jump state_7_bad_ending


##############################################################
#  STATE 02 — INVESTIGATE (Cabang Aksi Cerdas)
##############################################################
label state_02_investigate:
    scene bg_hp_whatsapp
    play sound "audio/gulp.wav"

    show hp_aku  at phone_enter_dual_left
    show hp_ibu  at phone_enter_dual_right
    show aku_foto   at char_active_left   with dissolve
    show ibu_foto   at char_passive_right with dissolve

    aku_chat "STOP BU! Jangan diklik. Kirim filenya ke aku, biar aku bongkar isinya."

    show aku_foto at char_passive_left  with dissolve
    show ibu_foto at char_active_right  with dissolve
    ibu_chat "Sudah Ibu kirim. Nomornya juga aneh, beda kode negara."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_foto

    scene bg_kamar_coding
    show aku_foto at char_active_center with dissolve
    "Aku tidak bisa membiarkan Ibu dalam bahaya.\nKarena aku memakai iPhone, file APK ini tidak bisa tereksekusi langsung,\ntapi aku bisa membedahnya di laptop."
    aku "Oke, mari kita lihat apa isi sebenarnya dari aplikasi bodong ini."
    hide aku_foto

    menu:
        "Verifikasi nomor pengirim dan jejak social engineering dulu":
            jump state_02a_verifikasi_pengirim

        "Buka Android Studio, bedah AndroidManifest.xml (Analisis Statis)":
            jump state_04_decompile

        "Jalankan APK di dalam Emulator Android (Analisis Dinamis)":
            jump state_05_emulator


##############################################################
#  STATE 02A — VERIFIKASI PENGIRIM
##############################################################
label state_02a_verifikasi_pengirim:
    scene bg_laptop_screen
    play sound "audio/mouse_clicks.wav"

    show aku_foto at char_active_center with dissolve
    "Aku mengecek nomor pengirim, domain tautan, dan pola bahasanya."

    sistem "Nomor terdeteksi dari VoIP luar negeri, tidak terkait instansi resmi."
    sistem "Pola pesan: urgensi palsu + ancaman denda + lampiran APK."

    aku "Jelas ini social engineering.\nMereka memancing panik agar korban klik tanpa berpikir."

    $ pengirim_terverifikasi = True
    $ bukti_terkumpul += 1

    "Aku simpan screenshot chat dan profil nomor sebagai bukti awal."
    hide aku_foto

    menu:
        "Lanjutkan analisis statis APK":
            jump state_04_decompile

        "Lanjutkan analisis dinamis lewat emulator":
            jump state_05_emulator


##############################################################
#  STATE 04 — DECOMPILE (Analisis Statis)
##############################################################
label state_04_decompile:
    scene bg_laptop_screen
    play sound "audio/sfx_keyboard.ogg"

    show aku_foto at char_active_center with dissolve
    "Aku melakukan decompile pada APK tersebut dan membuka file AndroidManifest.xml."

    sistem "Mendeteksi permission:\n  <uses-permission android:name='android.permission.RECEIVE_SMS'/>"
    sistem "Mendeteksi permission:\n  <uses-permission android:name='android.permission.SEND_SMS'/>"

    aku "Bingo! Aplikasi 'Undangan' ini diam-diam meminta akses\nuntuk membaca dan mengirim SMS."
    aku "Ini cara mereka mencuri kode OTP dari bank!"

    if not analisis_statis_selesai:
        $ bukti_terkumpul += 1
    $ analisis_statis_selesai = True

    play sound "audio/mouse_clicks.wav"
    "Aku men-screenshot baris kode berbahaya itu."
    hide aku_foto

    jump state_05b_pilih_lanjutan


##############################################################
#  STATE 05 — EMULATOR (Analisis Dinamis)
##############################################################
label state_05_emulator:
    scene bg_laptop_screen
    play sound "audio/sfx_keyboard.ogg"

    show aku_foto at char_active_center with dissolve
    "Aku memasukkan APK tersebut ke dalam emulator terisolasi di laptop\nagar aman dari data pribadiku."
    "Saat aplikasi dibuka, ia menampilkan layar loading palsu berkedok\n'Sedang Mengunduh Foto Undangan'."

    sistem "Peringatan: Aplikasi berjalan di background dan mencoba mengakses layanan SMS."

    aku "Gila, UI-nya sengaja dibuat loading lama agar korban tidak sadar\naplikasi ini sedang menyedot data SMS di background."

    if not analisis_dinamis_selesai:
        $ bukti_terkumpul += 1
    $ analisis_dinamis_selesai = True

    play sound "audio/sound.wav"
    "Aku merekam layar emulator tersebut sebagai bukti kerja malware-nya."
    hide aku_foto

    jump state_05b_pilih_lanjutan


##############################################################
#  STATE 05B — FSM LOOP ANALISIS
##############################################################
label state_05b_pilih_lanjutan:
    scene bg_kamar_coding
    show aku_foto at char_active_center with dissolve
    "Aku sudah dapat sebagian bukti.\nUntuk menjelaskan ke Ibu dengan meyakinkan, aku perlu memilih langkah berikutnya."
    hide aku_foto

    if analisis_statis_selesai and not analisis_dinamis_selesai:
        menu:
            "Lanjut analisis dinamis di emulator agar bukti lebih kuat":
                jump state_05_emulator
            "Cukup, langsung edukasi Ibu sekarang":
                jump state_06_edukasi

    elif analisis_dinamis_selesai and not analisis_statis_selesai:
        menu:
            "Lanjut analisis statis di manifest agar bukti teknis lengkap":
                jump state_04_decompile
            "Cukup, langsung edukasi Ibu sekarang":
                jump state_06_edukasi

    else:
        show aku_foto at char_active_center with dissolve
        "Bukti teknis sudah lengkap:\njejak social engineering, permission berbahaya, dan perilaku malware di emulator."
        hide aku_foto
        jump state_06_edukasi


##############################################################
#  STATE 06 — EDUKASI IBU (Telepon)
##############################################################
label state_06_edukasi:
    scene bg_hp_call
    play sound "audio/gulp.wav"

    show hp_aku at phone_enter_dual_left
    show hp_ibu at phone_enter_dual_right

    "Dengan bukti yang sudah kukumpulkan, aku menelepon Ibu dan menjelaskannya."

    if bukti_terkumpul > 0:
        show aku_foto  at char_active_left   with dissolve
        show ibu_panik at char_passive_right with dissolve

        aku "Lihat ini Bu — aplikasi ini dirancang khusus untuk\nmembaca kotak masuk SMS Ibu."
        aku "Kalau Ibu klik install, setiap kode OTP dari M-Banking yang masuk\nakan otomatis dikirim ke si penipu tanpa Ibu sadari."

        if pengirim_terverifikasi:
            aku "Aku juga sudah cek nomor pengirimnya.\nItu bukan nomor resmi — VoIP luar negeri yang dipakai menipu massal."

        show aku_foto  at char_passive_left  with dissolve
        show ibu_panik at char_active_right  with dissolve

        ibu "Astaghfirullah! Pantesan banyak yang uangnya ludes.\nMakasih ya Nak, Ibu langsung blokir nomornya."

        $ ibu_paham = True

        show aku_foto  at char_active_left   with dissolve
        show ibu_panik at char_passive_right with dissolve

    else:
        show aku_foto  at char_active_left   with dissolve
        show ibu_panik at char_passive_right with dissolve

        aku "Pokoknya ini bahaya Bu, bisa nyuri data."

        show aku_foto  at char_passive_left  with dissolve
        show ibu_panik at char_active_right  with dissolve

        ibu "Oh gitu, ngeri juga ya."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_panik

    jump state_05c_follow_up_keamanan


##############################################################
#  STATE 05C — FOLLOW-UP KEAMANAN
##############################################################
label state_05c_follow_up_keamanan:
    scene bg_hp_whatsapp
    play sound "audio/gulp.wav"

    show hp_aku  at phone_enter_dual_left
    show hp_ibu  at phone_enter_dual_right
    show aku_foto   at char_active_left   with dissolve
    show ibu_foto   at char_passive_right with dissolve

    aku_chat "Bu, sekarang buka pengaturan keamanan.\nMatikan izin instalasi dari sumber tidak dikenal."

    show aku_foto at char_passive_left  with dissolve
    show ibu_foto at char_active_right  with dissolve
    ibu_chat "Sudah. Ibu juga sudah ganti PIN m-banking dan aktifkan notifikasi transaksi."

    show aku_foto at char_active_left   with dissolve
    show ibu_foto at char_passive_right with dissolve
    aku_chat "Bagus! Kita juga laporkan nomor ini ke bank dan platform chat-nya ya."

    play sound "audio/sfx_error.ogg"
    show hp_ibu at phone_enter_bottom_alert

    aku_chat "Nah, ini contoh notifikasi darurat resmi dari bank.\nKalau muncul lagi, jangan panik — langsung verifikasi ke call center resmi."

    hide hp_aku
    hide hp_ibu
    hide aku_foto
    hide ibu_foto

    $ ibu_paham = True
    jump state_10_pilihan_akhir


##############################################################
#  STATE 10 — PILIHAN AKHIR PASCA-EDUKASI
##############################################################
label state_10_pilihan_akhir:
    scene bg_keluarga
    show aku_foto at char_active_center with dissolve
    "Ancaman langsung sudah ditangani.\nSekarang aku harus memilih dampak jangka panjangnya."
    hide aku_foto

    menu:
        "Tidur — yang penting Ibuku sudah aman.":
            jump state_8_neutral_ending

        "Bantu Ibu lapor resmi ke bank dan kanal aduan siber.":
            jump state_11_good_ending

        "Buat broadcast edukasi ke Grup Keluarga beserta screenshot bukti.":
            jump state_9_true_ending


##############################################################
#  STATE 7 — BAD ENDING: CYBER HEIST
##############################################################
label state_7_bad_ending:
    stop music fadeout 2.0
    scene bg_hacked
    play music "audio/fireplace.mp3" loop fadein 1.0

    show aku_foto at char_active_center with dissolve
    aku "Aku meremehkan rasa penasaran orang tua.\nHarusnya aku menjelaskan bahayanya, bukan sekadar melarang."
    hide aku_foto

    "Uang tabungan Ibu lenyap tak bersisa.\nModus rekayasa sosial ({i}social engineering{/i}) menang kali ini."
    "{b}*** BAD ENDING: CYBER HEIST ***{/b}"
    return


##############################################################
#  STATE 8 — NEUTRAL ENDING: MISSED OPPORTUNITY
##############################################################
label state_8_neutral_ending:
    stop music fadeout 2.0
    scene bg_kamar_gelap

    show aku_foto at char_active_center with dissolve
    "Aku menutup laptop dan tidur. Uang Ibuku aman."
    "Namun keesokan harinya aku mendengar kabar bahwa Tante dan Pakde di kampung\nterkena penipuan yang sama karena aku tidak mengingatkan mereka."
    hide aku_foto

    "{b}*** NEUTRAL ENDING: MISSED OPPORTUNITY ***{/b}"
    return


##############################################################
#  STATE 9 — TRUE GOOD ENDING: THE DIGITAL GUARDIAN
##############################################################
label state_9_true_ending:
    stop music fadeout 2.0
    scene bg_aman
    play music "audio/london_bridge.wav" loop fadein 1.0

    show aku_foto at char_active_left  with dissolve
    show ibu_lega at char_active_right with dissolve

    "Pesan dikirim ke grup: {i}Keluarga Harmonis{/i}."
    "Aku membagikan bukti screenshot dan penjelasan teknis\ndengan bahasa sederhana ke seluruh grup keluarga."
    "Banyak paman dan bibi yang berterima kasih —\nmereka baru saja akan membuka file serupa."

    aku "Dengan sedikit ilmu mobile programming, aku bukan cuma mengamankan sistem,\ntapi juga memperkuat literasi digital orang-orang terdekatku."

    show aku_foto at char_passive_left  with dissolve
    show ibu_lega at char_active_right  with dissolve
    ibu "Ibu bangga punya anak seperti kamu, Nak."

    hide aku_foto
    hide ibu_lega

    "{b}*** TRUE GOOD ENDING: THE DIGITAL GUARDIAN ***{/b}"
    return


##############################################################
#  STATE 11 — GOOD ENDING: INCIDENT CONTAINED
##############################################################
label state_11_good_ending:
    stop music fadeout 2.0
    scene bg_aman
    play music "audio/park.mp3" loop fadein 1.0

    show aku_foto at char_active_left  with dissolve
    show ibu_lega at char_active_right with dissolve

    "Aku membantu Ibu menghubungi bank, mengganti kredensial,\ndan melaporkan nomor penipu ke kanal aduan resmi."
    "Laporan kami dipakai sebagai data pola penipuan baru\nberbasis APK undangan palsu."

    show aku_foto at char_passive_left  with dissolve
    show ibu_lega at char_active_right  with dissolve
    ibu "Makasih ya Nak. Ibu jadi lebih tenang sekarang."

    show aku_foto at char_active_left   with dissolve
    show ibu_lega at char_passive_right with dissolve
    aku "Sama-sama Bu. Kalau ada yang aneh lagi, langsung tanya aku ya."

    hide aku_foto
    hide ibu_lega

    "{b}*** GOOD ENDING: INCIDENT CONTAINED ***{/b}"
    return
