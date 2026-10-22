from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

from routes.auth_routes import auth_bp
from routes.donation_routes import donation_bp
from routes.request_routes import request_bp
from routes.delivery_routes import delivery_bp
from routes.analytics_routes import analytics_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS for all API endpoints
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(donation_bp, url_prefix="/api/donations")
    app.register_blueprint(request_bp, url_prefix="/api/requests")
    app.register_blueprint(delivery_bp, url_prefix="/api/deliveries")
    app.register_blueprint(analytics_bp, url_prefix="/api/analytics")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(user_bp, url_prefix="/api/users")

    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "healthy",
            "service": "FoodRescue API",
            "database": "MongoDB (foodrescue_db)",
            "version": "1.0.0"
        }), 200

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app

app = create_app()

if __name__ == "__main__":
    print(f"🚀 FoodRescue Backend running on http://localhost:{Config.PORT}")
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)
