def read_url(url, cookie={"name" : "name", "value" : "value"}):
    cookie.update({"domain" : "127.0.0.1"})
    try :
        service = Service(executable_path="/chromedriver")
        options = webdriver.ChromeOptions()
        for _in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ] :
            options.add_argument(_)
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        driver.quit()
        # return False
    driver.quit()
    return True

def check_xss(param, cookie={"name" : "name", "value" : "value"}):
    url = f"http://127.0.0.1:8000/vuln?param={urlib.parse.quote(param)}"
    return read_url(url, cookie)

@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "GET":
        return render_template("flag.html")
    elif request.method == "POST":
        param = request.form.get("param")
        if not check_xss(param, {"name" : "flag", "value" : FLAG.strip()}):
            return '<script>alert("wrong??"); history.go(-1);</script>'
        return '<script>alert("good");history.go(-1);</script>'