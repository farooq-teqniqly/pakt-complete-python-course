def starts_with(s: str, str_to_eval: str, case_sensitive=False):
    if not case_sensitive:
        return str_to_eval.lower().startswith(s.lower())

    return str_to_eval.startswith(s)


if __name__ == "__main__":
    makes = ["BMW", "Ford", "Dodge", "Mercedes-Benz", "Mercury"]

    starts_with_mer = filter(lambda s: starts_with("mer", s), makes)
    mercedes = (make for make in starts_with_mer if len(make) > 7)
    print(list(mercedes))
