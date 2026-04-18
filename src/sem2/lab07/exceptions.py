class ItemNotFoundError(Exception):
    """Книга не найдена."""
    pass


class DuplicateItemError(Exception):
    """Такая книга уже существует."""
    pass