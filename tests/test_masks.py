from src.masks import mask_account, mask_card

card_number = "1111222233334444"
account_number = "1111222233334444"


def test_mask_account():
    assert mask_account(account_number) == "**4444"


def test_mask_card():
    assert mask_card(card_number) == "1111 22** **** 4444"
