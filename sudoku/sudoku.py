from flask import Flask, render_template, request, send_from_directory, redirect
from flask_sitemap import Sitemap
from datetime import datetime
import json
import content
from sudoku_logic import check_num_can_be_fill, fill_sudoku, create_empty_sudoku, create_sudoku_puzle

app = Flask(__name__)

sitemap = Sitemap(app=app)
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
app.config['SITEMAP_URL_SCHEME'] = 'https'
app.config['SITEMAP_CHANGE_FREQ'] = 'weekly'
app.config['SITEMAP_PRIORITY'] = 0.5

currentdate = datetime.today()
context = {
            'title':'Sudoku Puzle Solver',
            'websitename':'www.SudokePuzler.com',
            'currentyear':currentdate.year,
            'instruction':"""""",
            }

@app.route('/index')
@app.route('/')
def home():
    sdk = create_empty_sudoku()
    if (fill_sudoku(sdk,0,0)):
        #solution = sdk
        sdk_board = create_sudoku_puzle(sdk)
        context['msg'] = "SOLVE THIS SUDOKU ???"
        return render_template('index.html', sdk_board=sdk_board, context=context)
    context['msg'] = "There is an error please try again."
    return render_template('index.html', context=context)
    

@app.route('/your-sudoku')
def your_sudoku():
    context['msg'] = "Fill Your Sudoku Fields ^!^"
    sdk_board = [[0 for i in range(9)] for j in range(9)]
    return render_template('index.html', sdk_board=sdk_board , context=context)

@app.route('/solution', methods=['GET','POST'])
def solution():
    try:
        sdk = json.loads(request.args.get('sdk_box'))
        if (fill_sudoku(sdk,0,0)):
            return json.dumps({"sdk":sdk, "msg":"worked"})
        else:
            return json.dumps({"msg":"Numbers are filled in wrong orders >:"})
    except:
        return json.dumps({"msg": "Please send a valid Sudoku Puzle."})
    
@app.route('/about')
def about():
    context['content'] = content.about_us
    return render_template('otherpages.html', context=context)

@app.route('/privacy-policy')
def privacy_policy():
    context['content'] = content.privacy_policy
    return render_template('otherpages.html', context=context)

@app.route('/disclaimer')
def disclaimer():
    context['content'] = content.disclaimer
    return render_template('otherpages.html', context=context)

@app.route('/terms-and-conditions')
def terms_and_conditions():
    context['content'] = content.terms_and_conditions
    return render_template('otherpages.html', context=context)

@app.route('/contactus')
def contactus():
    context['content'] = content.contactus
    return render_template('otherpages.html', context=context)

@app.route('/sitemap.xml')
def sitemap_xml():
    return sitemap.sitemap()

# def static_from_root():
#     return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run(debug = True)
