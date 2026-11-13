
from django.shortcuts import render
from .ai_service import generate_email

def home(request):
    result = ""

    if request.method == "POST":
        prompt = request.POST.get("prompt", "")

        if prompt:
            try:
                result = generate_email(prompt)
            except Exception as e:
                result = f"Error generating email: {e}"

    return render(request, "assistant/home.html", {
        "result": result
    })
