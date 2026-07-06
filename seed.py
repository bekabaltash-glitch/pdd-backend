from app.database import SessionLocal, create_tables
from app.models.question import Question

def seed():
    create_tables()
    db = SessionLocal()
    
    # Check if already seeded
    if db.query(Question).count() > 0:
        print("Деректер базасы толтырылған")
        return
    
    questions = [
        Question(
            text_kz="Жол қозғалысы ережелері бойынша қызыл шамда не істеу керек?",
            text_ru="Что нужно делать на красный сигнал светофора по ПДД?",
            option_a_kz="Жылдамдықты азайтып өту",
            option_b_kz="Тоқтау",
            option_c_kz="Жылдамдықты арттырып өту",
            option_d_kz="Сигнал беріп өту",
            option_a_ru="Проехать, снизив скорость",
            option_b_ru="Остановиться",
            option_c_ru="Проехать, увеличив скорость",
            option_d_ru="Проехать, подав сигнал",
            correct_answer="b",
            category="rules",
            explanation_kz="Қызыл шамда міндетті түрде тоқтау керек.",
            explanation_ru="На красный сигнал необходимо остановиться."
        ),
        Question(
            text_kz="Тұрғын аймақта рұқсат етілген ең жоғары жылдамдық қанша?",
            text_ru="Какова максимальная скорость в жилой зоне?",
            option_a_kz="20 км/сағ",
            option_b_kz="30 км/сағ",
            option_c_kz="40 км/сағ",
            option_d_kz="60 км/сағ",
            option_a_ru="20 км/ч",
            option_b_ru="30 км/ч",
            option_c_ru="40 км/ч",
            option_d_ru="60 км/ч",
            correct_answer="a",
            category="rules",
            explanation_kz="Тұрғын аймақта ең жоғары жылдамдық 20 км/сағ.",
            explanation_ru="В жилой зоне максимальная скорость 20 км/ч."
        ),
        Question(
            text_kz="Қауіпсіздік белдігін кім тағуы керек?",
            text_ru="Кто обязан пристегнуть ремень безопасности?",
            option_a_kz="Тек жүргізуші",
            option_b_kz="Тек алдыңғы орындықтағылар",
            option_c_kz="Барлық жолаушылар мен жүргізуші",
            option_d_kz="Белдік міндетті емес",
            option_a_ru="Только водитель",
            option_b_ru="Только на передних сиденьях",
            option_c_ru="Все пассажиры и водитель",
            option_d_ru="Ремень не обязателен",
            correct_answer="c",
            category="rules",
            explanation_kz="Барлық жолаушылар мен жүргізуші белдік тағуы міндетті.",
            explanation_ru="Все пассажиры и водитель обязаны пристегнуться."
        ),
        Question(
            text_kz="Өту артықшылығын кім береді - бұл не дегенді білдіреді?",
            text_ru="Что означает 'уступить дорогу'?",
            option_a_kz="Жолды толық тосу",
            option_b_kz="Басқа көлікке кедергі жасамау",
            option_c_kz="Тоқтап, сигнал беру",
            option_d_kz="Артқа қайту",
            option_a_ru="Полностью остановиться",
            option_b_ru="Не создавать помех другому транспорту",
            option_c_ru="Остановиться и подать сигнал",
            option_d_ru="Сдать назад",
            correct_answer="b",
            category="rules",
            explanation_kz="Өту артықшылығы беру — басқа көлікке кедергі жасамау.",
            explanation_ru="Уступить дорогу — не создавать помех другому транспорту."
        ),
        Question(
            text_kz="Қалалық жолда рұқсат етілген ең жоғары жылдамдық?",
            text_ru="Максимальная скорость на городской дороге?",
            option_a_kz="60 км/сағ",
            option_b_kz="80 км/сағ",
            option_c_kz="90 км/сағ",
            option_d_kz="100 км/сағ",
            option_a_ru="60 км/ч",
            option_b_ru="80 км/ч",
            option_c_ru="90 км/ч",
            option_d_ru="100 км/ч",
            correct_answer="a",
            category="rules",
            explanation_kz="Қалалық жолда ең жоғары жылдамдық 60 км/сағ.",
            explanation_ru="На городской дороге максимальная скорость 60 км/ч."
        ),
    ]
    
    db.add_all(questions)
    db.commit()
    print(f"{len(questions)} сұрақ қосылды!")
    db.close()

if __name__ == "__main__":
    seed()
