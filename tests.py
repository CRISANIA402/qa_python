import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', [
        'А' * 40,
        'Книга',
    ])
    def test_add_new_book_valid_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        'А' * 41,
    ])
    def test_add_new_book_invalid_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_new_book("Властелин колец")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Мизери")
        collector.set_book_genre("Мизери", "Ужасы")
        assert collector.get_book_genre("Мизери") == "Ужасы"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")
        collector.set_book_genre("Книга без жанра", "Некорректный жанр")
        assert collector.get_book_genre("Книга без жанра") == ""

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Сияние']

    def test_get_books_for_children(self):
       collector = BooksCollector()
       collector.add_new_book('Мизери')
       collector.add_new_book('Шерлок Холмс')
       collector.add_new_book('Звездные войны')
       collector.set_book_genre('Мизери', 'Ужасы')
       collector.set_book_genre('Шерлок Холмс', 'Детективы')
       collector.set_book_genre('Звездные войны', 'Фантастика')
       assert collector.get_books_for_children() == ['Звездные войны']

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Книга избранное")
        collector.add_book_in_favorites("Книга избранное")
        assert "Книга избранное" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_not_in_collection(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Книга без коллекции")
        assert "Книга без коллекции" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")

        collector.delete_book_from_favorites("Книга 1")

        favorites = collector.get_list_of_favorites_books()
        assert "Книга 1" not in favorites
        assert "Книга 2" in favorites
    