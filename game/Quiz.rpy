

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

screen quiz_2():
    imagebutton:
        auto "back_btn_ref_%s.png"
        action Jump("soal_quiz_2")
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        imagebutton:
            auto "images/quiz/quiz_2_1_%s.png"
            action Jump("jawaban_soal_2_1")
        imagebutton:
            auto "images/quiz/quiz_2_2_%s.png"
            action Jump("jawaban_soal_2_2")

init python:
    import random
    status = [
        False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
    ]
    def random_pos():
        x = random.randint(0,300)
        y = random.randint(50,600)
        return (x,y)
    def drag_function(drags_items,drop_items):
        if drop_items is not None:
            if drags_items[0].drag_name == "piece_1" and drop_items.drag_name == "location_1":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[0] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_2" and drop_items.drag_name == "location_2":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[1] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_3" and drop_items.drag_name == "location_3":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[2] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_4" and drop_items.drag_name == "location_4":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[3] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_5" and drop_items.drag_name == "location_5":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[4] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_6" and drop_items.drag_name == "location_6":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[5] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_7" and drop_items.drag_name == "location_7":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[6] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_8" and drop_items.drag_name == "location_8":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[7] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_9" and drop_items.drag_name == "location_9":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[8] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_10" and drop_items.drag_name == "location_10":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[9] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_11" and drop_items.drag_name == "location_11":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[10] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_12" and drop_items.drag_name == "location_12":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[11] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_13" and drop_items.drag_name == "location_13":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[12] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_14" and drop_items.drag_name == "location_14":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[13] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_15" and drop_items.drag_name == "location_15":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[14] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")
            if drags_items[0].drag_name == "piece_16" and drop_items.drag_name == "location_16":
                drags_items[0].snap(drop_items.x,drop_items.y,0.5)
                status[15] = True
                if all(status) == True:
                    renpy.call("chapter_3_gunung")

screen puzzle_drag_1():
    image "images/puzzle_parang/bg_puzzle_parang.png"
    text "Susun Puzzle Batik Parang":
        xalign 0.5
        yalign 0.03
    $ pos1 = random_pos()
    $ pos2 = random_pos()
    $ pos3 = random_pos()
    $ pos4 = random_pos()
    $ pos5 = random_pos()
    $ pos6 = random_pos()
    $ pos7 = random_pos()
    $ pos8 = random_pos()
    $ pos9 = random_pos()
    $ pos10 = random_pos()
    $ pos11 = random_pos()
    $ pos12 = random_pos()
    $ pos13 = random_pos()
    $ pos14 = random_pos()
    $ pos15 = random_pos()
    $ pos16 = random_pos()
    draggroup:
        drag:
            xpos pos1[0]
            ypos pos1[1]
            drag_name "piece_1"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_1.png"
        drag:
            xpos pos2[0]
            ypos pos2[1]
            drag_name "piece_2"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_2.png"
        drag:
            xpos pos3[0]
            ypos pos3[1]
            drag_name "piece_3"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_3.png"
        drag:
            xpos pos4[0]
            ypos pos4[1]
            drag_name "piece_4"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_4.png"
        drag:
            xpos pos5[0]
            ypos pos5[1]
            drag_name "piece_5"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_5.png"
        drag:
            xpos pos6[0]
            ypos pos6[1]
            drag_name "piece_6"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_6.png"
        drag:
            xpos pos7[0]
            ypos pos7[1]
            drag_name "piece_7"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_7.png"
        drag:
            xpos pos8[0]
            ypos pos8[1]
            drag_name "piece_8"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_8.png"
        drag:
            xpos pos9[0]
            ypos pos9[1]
            drag_name "piece_9"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_9.png"
        drag:
            xpos pos10[0]
            ypos pos10[1]
            drag_name "piece_10"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_10.png"
        drag:
            xpos pos11[0]
            ypos pos11[1]
            drag_name "piece_11"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_11.png"
        drag:
            xpos pos12[0]
            ypos pos12[1]
            drag_name "piece_12"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_12.png"
        drag:
            xpos pos13[0]
            ypos pos13[1]
            drag_name "piece_13"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_13.png"
        drag:
            xpos pos14[0]
            ypos pos14[1]
            drag_name "piece_14"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_14.png"
        drag:
            xpos pos15[0]
            ypos pos15[1]
            drag_name "piece_15"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_15.png"
        drag:
            xpos pos16[0]
            ypos pos16[1]
            drag_name "piece_16"
            drag_raise True
            dragged drag_function
            add "images/puzzle_parang/Parang_16.png"
        
        
        #----- drop target -----

        drag:
            drag_name "location_1"
            draggable False
            align(0.5,0.1)
            add "images/puzzle_drag_parang/location_1.png"
        drag:
            drag_name "location_2"
            draggable False
            align(0.6,0.1)
            add "images/puzzle_drag_parang/location_2.png"
        drag:
            drag_name "location_3"
            draggable False
            align(0.7,0.1)
            add "images/puzzle_drag_parang/location_3.png"
        drag:
            drag_name "location_4"
            draggable False
            align(0.8,0.1)
            add "images/puzzle_drag_parang/location_4.png"
        
        # --- baris 1
        drag:
            drag_name "location_5"
            draggable False
            align(0.5,0.25)
            add "images/puzzle_drag_parang/location_5.png"
        drag:
            drag_name "location_6"
            draggable False
            align(0.6,0.25)
            add "images/puzzle_drag_parang/location_6.png"
        drag:
            drag_name "location_7"
            draggable False
            align(0.7,0.25)
            add "images/puzzle_drag_parang/location_7.png"
        drag:
            drag_name "location_8"
            draggable False
            align(0.8,0.25)
            add "images/puzzle_drag_parang/location_8.png"
        
        # baris 2
        drag:
            drag_name "location_9"
            draggable False
            align(0.5,0.5)
            add "images/puzzle_drag_parang/location_9.png"
        drag:
            drag_name "location_10"
            draggable False
            align(0.6,0.5)
            add "images/puzzle_drag_parang/location_10.png"
        drag:
            drag_name "location_11"
            draggable False
            align(0.7,0.5)
            add "images/puzzle_drag_parang/location_11.png"
        drag:
            drag_name "location_12"
            draggable False
            align(0.8,0.5)
            add "images/puzzle_drag_parang/location_12.png"
        
        # baris 3

        drag:
            drag_name "location_13"
            draggable False
            align(0.5,0.65)
            add "images/puzzle_drag_parang/location_13.png"
        drag:
            drag_name "location_14"
            draggable False
            align(0.6,0.65)
            add "images/puzzle_drag_parang/location_14.png"
        drag:
            drag_name "location_15"
            draggable False
            align(0.7,0.65)
            add "images/puzzle_drag_parang/location_15.png"
        drag:
            drag_name "location_16"
            draggable False
            align(0.8,0.65)
            add "images/puzzle_drag_parang/location_16.png"
