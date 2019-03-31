from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from tutorial.config.config import config
from tutorial.db import *

DSN = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    Base.metadata.create_all(engine)


def sample_data(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add_all(
        [
            Type("Byte", "0", "255", "unsigned", 1, ""),
            Type("ShortInt", "-128", "127", "signed", 1, ""),
            Type(
                "SmallInt",
                "-32768",
                "32767",
                "signed",
                2,
                "Может не существовать; вместо него Integer с тем же диапазоном",
            ),
            Type("Word", "0", "65535", "unsigned", 2, ""),
            Type("LongWord", "0", "4294967295", "unsigned", 4, ""),
            Type("LongInt", "-2147483648", "2147483647", "signed", 4, ""),
            Type(
                "Int64", "-9223372036854775808", "9223372036854775807", "signed", 8, ""
            ),
            Type("QWord", "0", "18446744073709551615", "unsigned", 8, ""),
            Type(
                "Integer",
                "-32768",
                "32767",
                "signed",
                2,
                "Наиболее быстрый целый; SmallInt или LongInt",
            ),
        ]
    )
    session.commit()
    session.add_all(
        [
            MathOperations(
                "Abs(x)",
                "целый вещественный",
                "целый вещественный",
                "Абсолютное значение 'х'",
            ),
            MathOperations("Sin(x)", "вещественный", "вещественный", "синус 'х' рад."),
            MathOperations(
                "Cos(x)", "вещественный", "вещественный", "косинус 'х' рад."
            ),
            MathOperations(
                "Arctan(x)",
                "вещественный",
                "вещественный",
                "арктангенс 'х' ( -Pi/2 <y< Pi/2 )",
            ),
            MathOperations(
                "Sqrt(x)", "вещественный", "вещественный", "квадратный корень из 'х'"
            ),
            MathOperations(
                "Sqr(x)",
                "целый вещественный",
                "целый вещественный",
                "значение 'х' в квадрате ( x2 )",
            ),
            MathOperations(
                "Power(a,x)",
                "вещественный",
                "вещественный",
                "значение 'a' в степени 'x' ( ax )",
            ),
            MathOperations(
                "Exp(x)",
                "вещественный",
                "вещественный",
                "значение 'е' в степени 'х' ( ex, где e= 2.718282... )",
            ),
            MathOperations(
                "Ln(x)",
                "вещественный",
                "вещественный",
                "натуральный логарифм 'х' ( х > 0 )",
            ),
            MathOperations(
                "Frac(x)", "вещественный", "вещественный", "дробная часть 'х'"
            ),
            MathOperations("Int(x)", "вещественный", "вещественный", "целая часть 'х'"),
            MathOperations(
                "Random", "-", "вещественный", "случайное число ( 0 <=y< 1 )"
            ),
            MathOperations("Random(x)", "Word", "Word", "случайное число ( 0 <=y< x )"),
            MathOperations(
                "Succ(c)", "порядковый", "порядковый", "следующий за 'с' символ"
            ),
            MathOperations(
                "Pred(c)", "порядковый", "порядковый", "предшествующий 'с' символ "
            ),
        ]
    )
    session.commit()

    session.add_all(
        [
            Class("MyClass1", 4, 7),
            Class("MyClass1", 3, 7),
            Class("MyClass2", 4, 3),
            Class("MyClass3", 2, 5),
            Class("MyClass4", 5, 6),
            Class("MyClass5", 7, 8),
            Class("MyClass6", 2, 4),
            Class("MyClass7", 3, 6),
            Class("MyClass8", 4, 7),
            Class("MyClass9", 1, 2),
            Class("MyClass10", 9, 5),
            Class("MyClass11", 4, 6),
        ]
    )
    session.commit()


if __name__ == "__main__":
    db_url = DSN.format(**config["postgres"])
    print(db_url)
    engine = create_engine(db_url)
    create_tables(engine)
    sample_data(engine)
