
screen quiz_1():
    hbox:
        xalign 0.5
        yalign 0.2
        spacing 100
        imagebutton:
            auto "images/quiz/quiz_1_1_%s.png"
            action Jump("jawaban_soal_1_1")
        imagebutton:
            auto "images/quiz/quiz_1_2_%s.png"
            action Jump("jawaban_soal_1_2")