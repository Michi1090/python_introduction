from pprint import pprint
import wikipedia, pprint

wikipedia.set_lang('ja')
result = wikipedia.summary('スマレジ')
print(result)

search_page = wikipedia.page('スマレジ')
pprint.pprint(search_page.content)
