import wikipedia, sys

wikipedia.set_lang('ja')
summary = wikipedia.summary(sys.argv[1], sentences = 1)
print(summary)

