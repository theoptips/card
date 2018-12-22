from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/<string:page_name>')
def render_static(page_name):
	print("debugging")
	print(page_name)
	#return render_template('%s.html' % page_name)
	return render_template('card.html')
 
if __name__ == '__main__':
	app.run()