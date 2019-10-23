def add_card(
    title="My card",
    description="My description",
    board_name="My board",
    list_name="My list",
    api_key="",
    api_secret="",
    token="",
    token_secret="any",
):
    """
    For this you need a Trello API key, secret and token. 
    Token secret can be any string, but should be altered for security purposes.
    """
    from trello import TrelloClient

    client = TrelloClient(
        api_key=api_key, api_secret=api_secret, token=token, token_secret=token_secret
    )

    trello_boards = client.list_boards()
    for trello_board in trello_boards:
        if trello_board.name == board_name:
            target_board = trello_board
            break

    trello_lists = target_board.all_lists()
    for trello_list in trello_lists:
        if trello_list.name == list_name:
            target_list = trello_list
            break

    target_list.add_card(title, desc=description)
