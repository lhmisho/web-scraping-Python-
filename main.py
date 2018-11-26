from webscrap import wlog, wscrap


wlog.set_custom_log_info('html/error.log')

# try:
#     raise Exception()
# except Exception as e:
#     wlog.report(e)

data_scrap = wscrap.Scrapper(wscrap.url_al, wlog)

# after first time retrieving data we i comment the retreive and write
#data_scrap.retrieve_data()
#data_scrap.write_data_in_html()


data_scrap.read_data_from_html()
data_scrap.convert_data_to_bs4()
#data_scrap.print_data()
data_scrap.parse_data_to_bs4()