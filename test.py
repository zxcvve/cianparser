import cianparser

vn_parser = cianparser.CianParser(location="Великий Новгород", output_format="json")
data = vn_parser.get_flats(
    deal_type="rent_long",
    rooms=(1, "studio"),
    with_saving_csv=True,
    additional_settings={"start_page": 1, "end_page": 2, "max_price": 30000},
)
