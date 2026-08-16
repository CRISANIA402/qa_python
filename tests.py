import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ""

    @pytest.mark.parametrize('name', [
        'А' * 40,
        'Книга',
    ])
    def test_add_new_book_valid_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        'А' * 41, ''
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

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        collector.add_new_book("Книга А")
        collector.add_new_book("Книга Б")
        collector.add_book_in_favorites("Книга А")     
        favorites_list = collector.get_list_of_favorites_books()
        assert "Книга А" in favorites_list
        assert "Книга Б" not in favorites_list

    def test_get_books_genre_returns_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        
        full_dict = collector.get_books_genre()
        assert isinstance(full_dict, dict)
        assert full_dict.get("Мастер и Маргарита") == "Фантастика"