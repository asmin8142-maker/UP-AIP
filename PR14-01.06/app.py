from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from markupsafe import escape

from config import APP_NAME, SECRET_KEY, DEBUG

from database import (
    init_db,
    get_all_items,
    add_item,
    delete_item,
    get_stats
)

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        date = request.form.get("date", "").strip()

        category = request.form.get("category", "").strip()

        amount = request.form.get("amount", "").strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        errors = []

        if not date:
            errors.append("Укажите дату.")

        if not category:
            errors.append("Укажите категорию.")

        if not amount:
            errors.append("Укажите сумму.")

        allowed_categories = (
            "Продукты",
            "Транспорт",
            "Развлечения",
            "Одежда",
            "Коммунальные услуги",
            "Другое"
        )

        if category not in allowed_categories:
            errors.append("Недопустимая категория.")

        try:
            amount = float(amount)

            if amount <= 0:
                errors.append(
                    "Сумма должна быть больше нуля."
                )

        except ValueError:
            errors.append(
                "Сумма должна быть числом."
            )

        if errors:

            for err in errors:
                flash(err, "error")

        else:

            add_item(
                date,
                category,
                amount,
                description
            )

            flash(
                "Расход успешно добавлен.",
                "success"
            )

        return redirect(url_for("index"))

    items = get_all_items()

    return render_template(
        "index.html",
        items=items,
        app_name=APP_NAME
    )


@app.route("/stats")
def stats():

    data = get_stats()

    return render_template(
        "stats.html",
        data=data,
        app_name=APP_NAME
    )


@app.route(
    "/delete/<int:item_id>",
    methods=["GET", "POST"]
)
def delete(item_id):

    if request.method == "POST":

        delete_item(item_id)

        flash(
            "Запись удалена.",
            "info"
        )

        return redirect(
            url_for("index")
        )

    return render_template(
        "confirm_delete.html",
        item_id=item_id,
        app_name=APP_NAME
    )


@app.route("/xss-demo")
def xss_demo():

    payload = "<script>alert('XSS')</script>"

    unsafe = payload

    safe_escaped = escape(payload)

    return render_template(
        "xss_demo.html",
        unsafe=unsafe,
        safe_escaped=safe_escaped,
        app_name=APP_NAME
    )


if __name__ == "__main__":

    init_db()

    app.run(debug=DEBUG)