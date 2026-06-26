import os
from flask import Flask

app = Flask(__name__)

# Get the environment name from docker-compose (default to Development if not found)
current_env = os.environ.get('ENV', 'development').upper()

@app.route('/')
def home():
    # Define custom descriptions for each Docker environment
    if current_env == 'DEVELOPMENT':
        purpose = "This container is used for active coding and feature building."
        actions = "Hot-reloading is enabled. Any changes made to the source code on your local machine will sync and reflect here instantly."
        bg_color = "#3b82f6" # Blue
    elif current_env == 'TESTING':
        purpose = "This container is dedicated to running automated unit tests and code coverage."
        actions = "It executes test suites against the latest codebase to ensure no bugs or breaking changes are introduced."
        bg_color = "#eab308" # Yellow
    else: # VALIDATION
        purpose = "This container serves as the final staging area before production deployment."
        actions = "It simulates a real production environment to perform user acceptance testing (UAT) and final quality assurance."
        bg_color = "#22c55e" # Green

    # Professional HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Environment: {current_env}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f6f9;
                margin: 0;
                padding: 40px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 80vh;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                max-width: 500px;
                width: 100%;
            }}
            .badge {{
                background-color: {bg_color};
                color: white;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 0.85rem;
                font-weight: bold;
                text-transform: uppercase;
                display: inline-block;
                margin-bottom: 15px;
            }}
            h1 {{ color: #1e293b; margin: 0 0 15px 0; font-size: 1.8rem; }}
            h3 {{ color: #475569; margin: 20px 0 5px 0; font-size: 1.1rem; }}
            p {{ color: #64748b; line-height: 1.6; margin: 0; font-size: 1rem; }}
            .footer {{ margin-top: 30px; font-size: 0.8rem; color: #94a3b8; text-align: center; border-top: 1px solid #e2e8f0; padding-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">{current_env} Environment</div>
            <h1>Docker Container Status</h1>
            
            <h3>What is this container for?</h3>
            <p>{purpose}</p>
            
            <h3>What happens here?</h3>
            <p>{actions}</p>
            
            <div class="footer">Powered by Docker Compose & Flask</div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # Run Flask on port 5000 inside the container, listening on all interfaces
    app.run(host='0.0.0.0', port=5000)
