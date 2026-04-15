from __future__ import annotations

from flask import Flask, jsonify, render_template


def create_app(shared_state: dict) -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("dashboard.html")

    @app.get("/api/status")
    def status():
        return jsonify(shared_state)

    return app
