class TestPhrase:
    def test_check_len_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) <15, "the gratest len of phrase"