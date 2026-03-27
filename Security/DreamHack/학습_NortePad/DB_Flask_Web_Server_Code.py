...
@app.route('/login', methods=['POST'])
def post_login():
    if 'username' in session:
        return redirect(url_for('get_login_success'))
    
    username = request.form.get('username')
    password = request.form.get('password')
-    if username in accounts and accounts[username] == password:
+    if check_account(username, password):
        session['username'] = username
        return redirect(url_for('get_login_success'))
    else:
        return redirect(url_for('get_login_failure'))
...