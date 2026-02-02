from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Lab Challenge: Survey Form")

# Static files and templates are already set up for you
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# TODO 1: Create a Pydantic model for the survey data (name, favorite_color, feedback)
# Hint: class SurveyData(BaseModel): ...


# TODO 2: Create a GET route at "/" that serves the survey.html template
# Hint: Use templates.TemplateResponse(request, "survey.html", {})


# =============================================================================
# SSR Endpoint (Server-Side Rendering)
# =============================================================================

# TODO 3: Create a POST route at "/submit-ssr" that:
#   - Receives form data (name, favorite_color, feedback) using Form(...)
#   - Returns survey.html template with the results (same page, inline results)
# Hint: return templates.TemplateResponse(request, "survey.html",
#           {"ssr_result": {"name": name, "favorite_color": favorite_color, "feedback": feedback}})


# =============================================================================
# API Endpoint (for JavaScript fetch)
# =============================================================================

# TODO 4: Create a POST route at "/submit-api" that:
#   - Receives JSON data using your Pydantic model
#   - Returns JSON response with the survey data
# Hint: async def submit_api(data: SurveyData):
#       return {"success": True, "name": data.name, ...}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
