from main import BooksCollector

class TestBooksCollector:
    def test_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        assert collector.books_rating == {'Война и Мир': 1}

    def test_add_the_same_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('Преступление и Наказание')
        assert collector.books_rating == {'Преступление и Наказание': 1}

    def test_set_book_rating_for_book_not_in_list_false(self):
        collector = BooksCollector()
        collector.set_book_rating('Aнна Каренина', 10)
        assert collector.books_rating == {}

    def test_set_book_rating_less_than_one_false(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.set_book_rating('Ведьмак', 0)
        assert collector.books_rating == {'Ведьмак': 1}

    def test_set_book_rating_more_than_ten_false(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_rating('Шерлок Холмс', 11)
        assert collector.books_rating == {'Шерлок Холмс': 1}

    def test_get_book_not_in_list_rating_false(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Великий Гэтсби') == None

    def test_get_books_with_specific_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Оливер Твист')
        collector.set_book_rating('Оливер Твист', 9)
        collector.add_new_book('Идиот')
        collector.add_new_book('Дюймовочка')
        collector.set_book_rating('Дюймовочка', 10)
        assert collector.get_books_with_specific_rating(9) == ['Оливер Твист']

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Ромео и Джульетта')
        collector.add_book_in_favorites('Ромео и Джульетта')
        assert collector.favorites == ['Ромео и Джульетта']

    def test_book_not_in_list_add_in_favorites_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Тихий Дон')
        assert collector.favorites == []

    def test_delete_book_from_favorite_true(self):
        collector = BooksCollector()
        collector.add_new_book('Тихий Дон')
        collector.add_book_in_favorites('Тихий Дон')
        collector.delete_book_from_favorites('Тихий Дон')
        assert collector.favorites == [] 