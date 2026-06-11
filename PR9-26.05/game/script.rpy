# 1. ОБЪЯВЛЕНИЕ ПЕРСОНАЖЕЙ И ИЗОБРАЖЕНИЙ
define p = Character("Елена Сергеевна", color="#c8ffc8")
define s = Character("Студент", color="#c8ffff")

# Подключение твоих 5 актуальных изображений
image bg street = "images/bg_street.jpg"
image teacher normal = "images/teacher.jpg"
image bg door = "images/bg_door.jpg"
image bg classroom = "images/bg_classroom.jpg"
image bg answer = "images/bg_answer.jpg"

# СТАРТ ИГРЫ
label start:
    scene black with fade
    "Глава 1: День Икс."
    "Сегодня решается судьба семестра. Лабораторная по нейросетям на флешке."
    jump scene_2_door

label scene_2_door:
    # Изображение растянется на весь экран
    scene bg door with dissolve
    "Вы стоите в пустом коридоре перед дверью кабинета."
    s "Так, главное не паниковать. Проект собран. Пора заходить."
    "Вы делаете глубокий вдох и стучите."
    jump scene_3_enter

label scene_3_enter:
    scene bg classroom with fade
    show teacher normal at right with dissolve
    s "Здравствуйте, Елена Сергеевна! Можно войти?"
    p "Входи. Присаживайся за свободный компьютер в конце класса."
    jump scene_5_show_project

label scene_5_show_project:
    scene bg answer with dissolve
    "Вы вставляете флешку, открываете среду разработки и запускаете проект."
    s "Елена Сергеевна, я всё подготовила. Новелла работает, графика на месте."
    jump scene_6_teacher_comes

label scene_6_teacher_comes:
    scene bg classroom with dissolve
    show teacher normal at center with move
    p "Отлично, давай посмотрим на твою структуру кода."
    jump scene_7_interrogation

label scene_7_interrogation:
    scene bg classroom
    show teacher normal at center
    p "А почему здесь используются именно эти метки? Объясни логику переходов."
    
    menu:
        "Ответить уверенно (Рассказать про архитектуру кода)":
            jump scene_8_good_answer
        "Занервничать (Признаться, что помогала нейросеть)":
            jump scene_9_bad_answer

label scene_8_good_answer:
    scene bg answer with dissolve
    s "Здесь всё просто! Мы инициализируем движок, передаем параметры и строим ветвление."
    jump scene_10_graphics_defense

label scene_9_bad_answer:
    scene bg answer with dissolve
    s "Ну... я частично использовала подсказки ИИ, чтобы оптимизировать структуру..."
    jump scene_10_graphics_defense

label scene_10_graphics_defense:
    scene bg classroom with dissolve
    show teacher normal at truecenter with dissolve
    p "Ладно. А как обстоят дела с генерацией фонов и персонажей?"
    s "Я использовала нейросеть Leonardo.ai, соблюдая пропорции 16:9 и единый аниме-стиль."
    p "Да, визуальный стиль подобран хорошо."
    jump scene_11_final_check

label scene_11_final_check:
    scene bg classroom with dissolve
    show teacher normal at right with dissolve
    p "А требования по количеству сцен и смене изображений выполнены?"
    s "Да, в коде прописаны все необходимые ветвления и переходы."
    jump scene_12_verdict

label scene_12_verdict:
    scene bg classroom with dissolve
    show teacher normal at center with move
    p "Что ж... Я вижу проделанную работу. Код чистый, проект объемный."
    jump scene_13_grade

label scene_13_grade:
    scene bg street with fade
    show teacher normal at center with dissolve
    p "Ставлю заслуженное «Отлично» за лабораторную работу!"
    s "Ура! Спасибо большое, Елена Сергеевна!"
    jump scene_14_epilogue

label scene_14_epilogue:
    scene bg street with dissolve
    "Вы выходите из университета на залитую солнцем улицу."
    "Лабораторная сдана, все требования выполнены!"
    scene black with fade
    "Конец игры. Спасибо за внимание!"
    return