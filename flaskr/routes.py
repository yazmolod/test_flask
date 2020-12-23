from flaskr import APP

@APP.route('/')
@APP.route('/index')
def index():
	print('index')
	return 'Hello world'

@APP.route('/kepler')
def datamap():
	with open('flaskr/templates/Карта.html', encoding='utf-8') as file:
		data = file.read()
	return data

@APP.route('/kepler_fix')
def datamap2():
	with open('flaskr/templates/Карта_changed.html', encoding='utf-8') as file:
		data = file.read()
	return data

if __name__ == '__main__':
	data = datamap()